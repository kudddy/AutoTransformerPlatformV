import asyncio
import time
from json import dumps
import logging
from aiohttp_requests import requests as async_req

try:
    from ..persistants.request_info import headers_sberauto
    from ..plugins.config import cfg
except Exception as e:
    from persistants.request_info import headers_sberauto
    from plugins.config import cfg


url = cfg.app.url.sberautogetcars


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)


def timing(f):
    def wrap(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        log.debug('{:s} function took {:.3f} ms'.format(f.__name__, (end - start) * 1000.0))
        return ret

    return wrap


def is_true(val):
    if val:
        return val


def generate_city_str(citys_id: list):
    city_str = ""
    for city in citys_id:
        city_str += "&city={}".format(city)
    return city_str


async def get_cars_from_sberauto(brand_id: int or bool,
                                 city_id: list or bool,
                                 model_id: int or bool,
                                 year_to: int or bool,
                                 year_from: int or bool,
                                 page: int):
    payload = {
        "filter": {
            "engine_type_code": [],
            "transmission_code": [],
            "transmission_drive_code": [],
            "color_code": [],
            "body_type_code": [],
            "label_code": [],
            "year_to": year_to if year_to else None,
            "year_from": year_from if year_from else None,
            "city_id": city_id if city_id else [],
            "is_new": None,
            "catalog": [
                {
                    "brand_id": brand_id,
                    "model_id": [model_id] if model_id else [],
                    "folder_id": []
                }
            ],
            "rental_car": "exclude_rental"
        },
        "per_page": 100,
        "sort_asc": False,
        "sort_by": "",
        "page": page
    }

    response = await async_req.post(url, headers=headers_sberauto, data=dumps(payload), ssl=False)

    # response = request("POST", url, headers=headers_sberauto, data=dumps(payload), ssl=False)

    return await response.json()


async def async_get(brand_id: int or bool,
                    city_id: list or bool,
                    model_id: int or bool,
                    year_to: int or bool,
                    year_from: int or bool):
    async_tasks = []
    for page in range(1, 30):
        async_tasks.append(get_cars_from_sberauto(
            brand_id=brand_id,
            city_id=city_id,
            model_id=model_id,
            year_from=year_from,
            year_to=year_to,
            page=page
        ))

    responses = await asyncio.gather(*async_tasks)
    return responses
