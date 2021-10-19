from plugins.duckling.handlers.money import TextMoney
from plugins.duckling.handlers.date import TextYear
from plugins.duckling.handlers.brand import TextBrands
from plugins.duckling.handlers.city import TextCity
from plugins.duckling.handlers.search_engine import CheckingReq
import pymorphy2


def text_list(user_text):
    """
    Разбивает фразу клиента на слова в виде списка

    :param user_text: Фраза клиента
    :return: ['найти', 'мерс', 'в', 'екатеринбург', 'от', '2012', 'до', '2022', 'год']
    """

    result = list()
    morph = pymorphy2.MorphAnalyzer()
    for word in user_text.split():
        result.append(morph.parse(word)[0].normal_form)  # Записываем в нормализованном виде
    return result


def dictionary_string(user_text):
    """
    Структурирует текст

    :return: {'brand_id': 229, 'model_id': [2789], 'city_id': None, 'year_from': None,
    'year_to': None, 'price_from': None, 'price_to': None}
    """
    result = TextBrands(text_list(user_text)).handler()
    result.update(TextCity(text_list(user_text)).handler())
    result.update(TextYear(user_text).handler())
    result.update(TextMoney(user_text).handler())
    print("мы тут")
    return result.get('brand_id', False), \
           result.get('model_id', False), \
           result.get('city_id', False), \
           result.get('year_from', False), \
           result.get('year_to', False)


def search_engine(text) -> dict:
    search_engine = CheckingReq(dictionary_string(text))  # Подключаем сберавто
    return search_engine.check_handler()
