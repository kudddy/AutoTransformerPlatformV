import unittest

from plugins.config import cfg
from plugins.inputer import inputter


class AioMemTest(unittest.TestCase):
    def test_success_resp_with_brand(self):
        test = {
            "MESSAGE_NAME": "GET_DUCKLING_RESULT",
            "data": {
                "text": "BMW"
            }
        }

        res = inputter(test)
        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

    def test_success_resp_brand_model(self):
        test = {
            "MESSAGE_NAME": "GET_DUCKLING_RESULT",
            "data": {
                "text": "bmw 3"
            }
        }

        res = inputter(test)
        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

    def test_success_resp_brand_model_city(self):
        test = {
            "MESSAGE_NAME": "GET_DUCKLING_RESULT",
            "data": {
                "text": "bmw 3 в москве"
            }
        }

        res = inputter(test)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

    def test_success_resp_brand_model_city_year_from(self):
        test = {
            "MESSAGE_NAME": "GET_DUCKLING_RESULT",
            "data": {
                "text": "bmw 3 в москве от 2015 года"
            }
        }

        res = inputter(test)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва от 2015 года")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2015)

    def test_success_resp_brand_model_city_year_to(self):
        test = {
            "MESSAGE_NAME": "GET_DUCKLING_RESULT",
            "data": {
                "text": "bmw 3 в москве до 2015"
            }
        }

        res = inputter(test)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва до 2015 года")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2015)

    def test_success_resp_brand_model_city_year_from_to(self):
        test = {
            "MESSAGE_NAME": "GET_DUCKLING_RESULT",
            "data": {
                "text": "bmw 3 в москве от 2015 до 2020"
            }
        }

        res = inputter(test)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва от 2015 до 2020 года")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2020)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2015)

    # def test_success_resp_city(self):
    #     test = {
    #         "MESSAGE_NAME": "GET_DUCKLING_RESULT",
    #         "data": {
    #             "text": "Москва"
    #         }
    #     }

        # res = inputter(test)
        #
        # self.assertEqual(res['PAYLOAD']['STATUS'], True)
        #
        # search_text_form = res['PAYLOAD']['result']['search_text_form']
        #
        # self.assertEqual(search_text_form, "Москва")


