import asyncio
from json import dumps
from statistics import median
from urllib.parse import quote
from aiohttp_requests import requests as async_req

try:
    from ..config import cfg
    from ..helper import generate_city_str, timing
    from ...persistants.request_info import headers_sberauto
    from ..loader import citys_map, marks_revers, models_revers
except Exception as e:
    from plugins.config import cfg
    from plugins.helper import generate_city_str, timing
    from persistants.request_info import headers_sberauto
    from plugins.loader import citys_map, marks_revers, models_revers

url = cfg.app.url.sberautogetcars

redirect_url_web = cfg.app.url.sberautomainweb

redirect_url_mobile = cfg.app.url.sberautomainios

loop = asyncio.get_event_loop()


class SberAutoLoader:
    def __init__(self,
                 brand_id: int or bool,
                 city_id: list or bool,
                 model_id: int or bool,
                 year_to: int or bool,
                 year_from: int or bool):
        self.brand_id = brand_id
        self.city_id = city_id
        self.model_id = model_id
        self.year_to = year_to
        self.year_from = year_from

    async def get_cars_from_sberauto(self, page: int):
        payload = {
            "filter": {
                "engine_type_code": [],
                "transmission_code": [],
                "transmission_drive_code": [],
                "color_code": [],
                "body_type_code": [],
                "label_code": [],
                "year_to": self.year_to if self.year_to else None,
                "year_from": self.year_from if self.year_from else None,
                "city_id": self.city_id if self.city_id else [],
                "is_new": None,
                "catalog": [
                    {
                        "brand_id": self.brand_id if self.brand_id else None,
                        "model_id": [self.model_id] if self.model_id else [],
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

    async def async_get(self) -> list:
        async_tasks = []
        for page in range(1, 30):
            async_tasks.append(self.get_cars_from_sberauto(
                page=page
            ))

        responses = await asyncio.gather(*async_tasks)
        return responses

    @timing
    def run_loop_and_prepare_data(self):
        responses = loop.run_until_complete(self.async_get())

        all_responses: list = []
        for data in responses:
            success = data.get("success")
            if success:
                response = data.get("data", {}).get("results", [])
                if response:
                    all_responses.extend(response)

        return all_responses


class SberAutoProcessor(SberAutoLoader):
    def __init__(self,
                 brand_id: int or bool,
                 city_id: list or bool,
                 model_id: int or bool,
                 year_to: int or bool,
                 year_from: int or bool):
        super().__init__(brand_id,
                         city_id,
                         model_id,
                         year_to,
                         year_from)

    def any_options_found(self):
        if self.brand_id or self.model_id or self.city_id or self.year_from or self.year_to:
            return True
        return False

    @staticmethod
    def get_min_max_middle_from_resp(search_res: list):
        min_price = None
        max_price = None
        middle_value = None
        count = None
        status = False
        if search_res is None:
            return status, min_price, max_price, count

        if len(search_res) > 0:
            prices = [x['price'] for x in search_res]
            min_price = min(prices)
            middle_value = median(prices)
            max_price = max(prices)
            count = len(prices)
            status = True
        else:
            status = False

        return status, min_price, middle_value, max_price, count if count else 0

    @staticmethod
    def encode_uri_component(formdata: str):
        return quote(formdata, safe='~()*!.\'')

    def generate_city_str(self):
        city_str = ""
        for city in self.city_id:
            city_str += "&city={}".format(city)
        return city_str

    def generate_url_for_mobile(self, find_anything: bool):

        if not find_anything:
            return "https://sberauto.com/app/chat/car_select"

        payload = {
            "engine_type_code": [],
            "transmission_code": [],
            "transmission_drive_code": [],
            "color_code": [],
            "body_type_code": [],
            "label_code": [],
            "year_to": self.year_to if self.year_to else None,
            "year_from": self.year_from if self.year_from else None,
            "city_id": self.city_id if self.city_id else [],
            "is_new": None,
            "catalog": [
                {
                    "brand_id": self.brand_id if self.brand_id else None,
                    "model_id": [self.model_id] if self.model_id else []
                }
            ]
        }

        form_data_string: str = ""
        for k, v in payload.items():
            if v:
                if isinstance(v, str):
                    form_data_string += "&{}='{}'".format(k, self.encode_uri_component(v))
                elif isinstance(v, dict) or isinstance(v, list):
                    form_data_string += "&{}={}".format(k, self.encode_uri_component(dumps(v, separators=(',', ':'))))
                else:
                    form_data_string += "&{}={}".format(k, v)
        return redirect_url_mobile + "?{}".format(form_data_string[1:])

    def generate_url(self, find_anything: bool) -> str:
        if not find_anything:
            return "https://sberauto.com/cars?"
        # генерация ссылки относительно входящий параметов
        if self.brand_id and self.city_id and self.model_id:
            city_str = generate_city_str(self.city_id)
            done_url = redirect_url_web + "?brand={}=model={}&rental_car=exclude_rental{}".format(self.brand_id,
                                                                                                  self.model_id,
                                                                                                  city_str)
        elif self.brand_id and self.model_id:
            done_url = redirect_url_web + "?brand={}=model={}&rental_car=exclude_rental".format(self.brand_id,
                                                                                                self.model_id)
        elif self.brand_id and self.city_id:
            city_str = generate_city_str(self.city_id)
            done_url = redirect_url_web + "?brand={}{}&rental_car=exclude_rental".format(self.brand_id,
                                                                                         city_str)
        elif self.brand_id:
            done_url = redirect_url_web + "?brand={}&rental_car=exclude_rental".format(self.brand_id)
        else:
            done_url = redirect_url_web + "?"
        if self.year_to or self.year_from:
            if self.year_to and self.year_from:
                done_url = done_url + "&dateTo={}&dateFrom={}".format(self.year_to, self.year_from)
            elif self.year_to:
                done_url = done_url + "&dateTo={}".format(self.year_to)
            elif self.year_from:
                done_url = done_url + "&dateFrom={}".format(self.year_from)
        return done_url

    def generate_text_form(self):
        done_str = ""
        if self.brand_id:
            done_str += "{}".format(models_revers[self.brand_id])
        if self.model_id:
            done_str += " {}".format(marks_revers[self.model_id])
        if self.city_id:
            local_str: str = ""
            for city in self.city_id:
                local_str += " {},".format(citys_map[city])
            if len(self.city_id) > 1:
                local_str = local_str[:-1]
            else:
                local_str = local_str[1:-1]
            done_str += " {}".format(local_str)

        # сначала рассматриваем вариант что есть от и до
        if self.year_to and self.year_from:
            if self.year_to == self.year_from:
                done_str += " {} года".format(self.year_to)
            else:
                done_str += " от {} до {} года".format(self.year_from, self.year_to)

        if self.year_to and not self.year_from:
            done_str += " до {} года".format(self.year_to)

        if not self.year_to and self.year_from:
            done_str += " от {} года".format(self.year_from)

        return done_str.lstrip().rstrip()
