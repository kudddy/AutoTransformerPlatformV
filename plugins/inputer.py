import logging
import asyncio

from ..plugins.responder.sberauto import \
    parse_response, generate_url, \
    generate_url_for_mobile, generate_text_form
from ..plugins.responder.autoru import get_search_res_yandex
from ..plugins.responder.tlg import send_message
from ..plugins.duckling.typonder import replace_typos
from ..plugins.config import cfg
from ..plugins.helper import async_get

tlg_logger = cfg.app.url.tlg

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

loop = asyncio.get_event_loop()


def inputter(res: object):
    log.debug(f'start process message with payload - {res}')
    result: dict = {}
    search_res_text_from = None

    text: str = res["data"]["text"]

    text = replace_typos(text)
    try:
        log.debug("message_name - %r info - %r", "GET_DUCKLING_RESULT", "token - {}".format(text))

        brand_id, model_id, city_id, year_from, year_to = get_search_res_yandex(text)

        # TODO подумать насчет этого условия

        if brand_id or model_id or city_id:
            # запускаем локальный цикл событий

            responses = loop.run_until_complete(async_get(brand_id=brand_id,
                                                          city_id=city_id,
                                                          model_id=model_id,
                                                          year_from=year_from,
                                                          year_to=year_to))

            all_responses: list = []
            for data in responses:
                success = data.get("success")
                if success:
                    response = data.get("data", {}).get("results", [])
                    if response:
                        all_responses.extend(response)

        else:
            status = False

            logger_string: str = "☢️ по токету - {} ничего не найдено".format(text)
            send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
            log.debug(f'function done work fine but nothing found')
            return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                    "STATUS": status,
                    "PAYLOAD": {
                        "result": result,
                        "description": "nothing found"
                    }}

        status, min_price, middle_value, max_price, count = parse_response(all_responses)

        # проверяем статус от сберавто по поводу найденых авто
        if status:
            if cfg.app.main.redirect_to_mobile:
                done_url = generate_url_for_mobile(brand_id,
                                                   city_id,
                                                   model_id,
                                                   year_from,
                                                   year_to)
            else:
                done_url = generate_url(brand_id,
                                        city_id,
                                        model_id,
                                        year_from,
                                        year_to)
            # генерируем текстовую форму

            search_res_text_from = generate_text_form(brand_id,
                                                      city_id,
                                                      model_id,
                                                      year_from,
                                                      year_to)

        else:
            if cfg.app.main.redirect_to_mobile:
                done_url = "https://sberauto.com/app/chat/car_select"
            else:
                done_url = "https://sberauto.com/cars?"

        # TODO слишком влияет на производительность
        logger_string: str = "✅по токету - {} OK".format(text)
        send_message(url=tlg_logger, text=logger_string, chat_id=81432612)

        log.debug(f'function done work fine')

        return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                "STATUS": status,
                "PAYLOAD": {
                    "result": {
                        "min_price": min_price,
                        "median": int(middle_value) if middle_value else None,
                        "max_price": max_price,
                        "count": count,
                        "url": done_url,
                        "search_text_form": search_res_text_from if search_res_text_from else False,
                        "search_keys": {
                            "brand_id": brand_id,
                            "city_id": city_id,
                            "model_id": model_id,
                            "year_from": year_from,
                            "year_to": year_to
                        },
                        # TODO надо что то придумать с пагинацией
                        "canvas_data": all_responses[:10]
                    },
                    "description": "OK"
                }}
    except Exception as e:
        log.debug("message_name - %r info - %r error - %r",
                  "GET_DUCKLING_RESULT",
                  "token - {}".format(text),
                  e)
        status = False
        logger_string: str = "🛑 по токету - {} ошибка - {}".format(text, str(e)[0:4095])
        send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
        logging.info(f'function done work incorrect')
        return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                "STATUS": status,
                "PAYLOAD": {
                    "result": result,
                    "description": "error"
                }}
