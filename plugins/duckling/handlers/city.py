from plugins.loader import city


class TextCity:

    def __init__(self, text):
        self.text_list = text  # Список слов: ['найти', 'мерс', 'в', 'екатеринбург']

    def city(self):
        """
        Находит как один город так и несколько.
        Справляется с поиском городов таких как Нижний Новгород через пробел

        :return: 'city_id': [1, 10]
        """
        city_list = list()

        for i in self.text_list:
            if city.get(i):
                city_list.append(city.get(i))

        for i in range(len(self.text_list) - 1):  # Находим города с пробелом: Нижний Новгород
            cities_space = f'{self.text_list[i]} {self.text_list[i + 1]}'
            if city.get(cities_space):
                city_list.append(city.get(cities_space))

        list_of_unique_id = []  # Проверим что все значения списка уникальные
        unique_numbers = set(city_list)
        for number in unique_numbers:
            list_of_unique_id.append(number)

        if len(list_of_unique_id) >= 1:  # Проверим что список не пустой
            return dict(city_id=list_of_unique_id)
        else:
            return dict(city_id=None)

    def handler(self):
        return self.city()
