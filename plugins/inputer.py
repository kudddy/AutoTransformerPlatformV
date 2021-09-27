import logging
import asyncio

try:
    from ..plugins.responder.sberauto import SberAutoProcessor
    from ..plugins.responder.autoru import get_search_res_yandex
    from ..plugins.responder.tlg import send_message
    from ..plugins.duckling.typonder import replace_typos
    from ..plugins.config import cfg
    from ..plugins.helper import async_get

except Exception as e:
    from plugins.responder.sberauto import SberAutoProcessor
    from plugins.responder.autoru import get_search_res_yandex
    from plugins.responder.tlg import send_message
    from plugins.duckling.typonder import replace_typos
    from plugins.config import cfg
    from plugins.helper import async_get

tlg_logger: str = cfg.app.url.tlg

use_tlg_logger: bool = cfg.app.main.use_tlg_logger

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

        sber_auto_processor = SberAutoProcessor(
            brand_id=brand_id,
            model_id=model_id,
            city_id=city_id,
            year_from=year_from,
            year_to=year_to
        )

        if sber_auto_processor.any_options_found():

            all_responses = sber_auto_processor.run_loop_and_prepare_data()

            search_res_text_from = sber_auto_processor.generate_text_form()

            status, min_price, middle_value, max_price, count = sber_auto_processor.get_min_max_middle_from_resp(
                all_responses)

            if count == 0:
                # TODO грязно
                status = False
                if use_tlg_logger:
                    logger_string: str = "☢️ токен - {} классифицирован, но в базе sberauto ничего не найдено".format(
                        text)
                    send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                log.debug(f'function done work fine but nothing found')
                return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                        "CODE": 404,
                        "STATUS": status,
                        "PAYLOAD": {
                            "result": {
                                "search_text_form": search_res_text_from if search_res_text_from else False
                            },
                            "description": "nothing found"
                        }}

        else:
            # TODO Кажется, что в это условие никогда не заходит
            status = False
            if use_tlg_logger:
                logger_string: str = "☢️ по токету - {} ничего не найдено".format(text)
                send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
            log.debug(f'function done work fine but nothing found')
            return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                    "CODE": 504,
                    "STATUS": status,
                    "PAYLOAD": {
                        "result": {
                            "search_text_form": search_res_text_from if search_res_text_from else False
                        },
                        "description": "nothing found"
                    }}

        # проверяем статус от сберавто по поводу найденых авто
        if cfg.app.main.redirect_to_mobile:
            done_url = sber_auto_processor.generate_url_for_mobile(status)
        else:
            done_url = sber_auto_processor.generate_url(status)

        # TODO слишком влияет на производительность
        if use_tlg_logger:
            logger_string: str = "✅по токету - {} OK".format(text)
            send_message(url=tlg_logger, text=logger_string, chat_id=81432612)

        log.debug(f'function done work fine')

        return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                "STATUS": status,
                "CODE": 200,
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
        if use_tlg_logger:
            logger_string: str = "🛑 по токету - {} ошибка - {}".format(text, str(e)[0:4095])
            send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
        logging.info(f'function done work incorrect with error - {e}')
        return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                "CODE": 504,
                "STATUS": status,
                "PAYLOAD": {
                    "result": result,
                    "description": "error"
                }}
