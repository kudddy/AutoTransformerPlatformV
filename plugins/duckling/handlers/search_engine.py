import requests
from json import dumps


class CheckingReq:

    def __init__(self, data_type=None):
        self.auto_id = data_type

    def response_sberato(self, headers_sberauto, payload):

        response = requests.post('https://api.sberauto.com/searcher/getCars', headers=headers_sberauto,
                                 data=dumps(payload))
        resp = response.json()

        try:
            if resp.get('success') == True:
                if resp.get('data').get('total') >= 1:
                    return resp
                else:
                    print('не найдено')

            else:
                print('False')

        except TypeError:
            print(f"\nЗапрос успешен: {resp.get('success')}\n"
                  f"Всего машин: {resp.get('data').get('total') if resp.get('data') else None}")

            print(resp.get('data').get('total') if resp.get('data') else None)

    def check_get_cars(self,
                       brand_id: int or bool,
                       model_id: list or bool,
                       city_id: list or bool,
                       year_from: int or bool,
                       year_to: int or bool,
                       price_from: int or bool,
                       price_to: int or bool):

        headers_sberauto = {
            "Content-Type": "application/json"
        }
        payload = {"page": 1,
                   "per_page": 1,
                   "filter": {
                       "engine_type_code": [],
                       "transmission_code": [],
                       "transmission_drive_code": [],
                       "color_code": [],
                       "body_type_code": [],
                       "label_code": [],
                       "price_from": price_from if price_from else None,
                       "price_to": price_to if price_to else None,
                       "year_from": year_from if year_from else None,
                       "year_to": year_to if year_to else None,
                       "city_id": city_id if city_id else [],
                       "is_new": None,
                       "catalog": [
                           {
                               "brand_id": brand_id if brand_id else None,
                               "model_id": model_id if model_id else None,
                               "folder_id": []
                           }
                       ],
                       "rental_car": "exclude_rental"
                   },
                   "sort_asc": False,
                   "sort_by": ""
                   }

        return self.response_sberato(headers_sberauto, payload)

    def check_dict(self):
        """

        :return: {'brand_id': 232, 'model_id': [2835], 'city_id': False,
        'year_from': False, 'year_to': False, 'price_from': False, 'price_to': False}
        """
        dict_list = ['brand_id', 'model_id', 'city_id', 'year_from', 'year_to', 'price_from', 'price_to']
        data = dict()

        for i in dict_list:
            if i in self.auto_id:
                data.update({i: self.auto_id.get(i) if self.auto_id.get(i) is not None else False})
            else:
                data.update({i: self.auto_id.get(i) if self.auto_id.get(i) is not None else False})

        return self.check_get_cars(brand_id=data.get('brand_id'),
                                   model_id=data.get('model_id'),
                                   city_id=data.get('city_id'),
                                   year_from=data.get('year_from'),
                                   year_to=data.get('year_to'),
                                   price_from=data.get('price_from'),
                                   price_to=data.get('price_to'))

    def check_handler(self):
        return self.check_dict()
