from plugins.loader import model as models


class TextBrands:

    def __init__(self, text):
        '''

        :param text: Список слов: ['найти', 'мерс', 'в', 'екатеринбург']
        '''
        self.text_list = text

    def brand(self):
        """
        Вытащит id тачки, если она есть иначе None

        :return: 232 or None
        """

        brand_list = list()
        model = models.get('brands')

        for i in self.text_list:
            if model.get(i):
                brand_list.append(model.get(i))

        for i in range(len(self.text_list) - 1):  # Находим тачки с пробелом: властелин колец
            x = f'{self.text_list[i]} {self.text_list[i + 1]}'
            if model.get(x):
                brand_list.append(model.get(x))

        list_of_unique_id = []  # Получаем уникальный id автомобиля
        unique_numbers = set(brand_list)
        for number in unique_numbers:  # Проверим, что все значения списка уникальные
            list_of_unique_id.append(number)

        if len(list_of_unique_id) >= 1:  # Проверим что найден один или более автомобилей
            return list_of_unique_id[0]
        else:
            return None

    def models_list(self):
        """
        Вытащит все id тачек и моделей (не уникальные)

        :return: [[232, 2835], [204, 2415], [204, 2415], [232, 2818]]
        """

        model = models.get('alias')
        models_list = list()

        for i in range(len(self.text_list) - 1):  # Находим модели с пробелом: сивка бурка
            x = f'{self.text_list[i]} {self.text_list[i + 1]}'
            if model.get(x):
                for m in model.get(x):
                    m_tuple = tuple(m)
                    models_list.append(m_tuple)

        for i in self.text_list:
            if model.get(i):
                for m in model.get(i):
                    m_tuple = tuple(m)
                    models_list.append(m_tuple)

        if len(models_list) == 0:
            return None
        else:
            return models_list

    def models_unique_list(self):
        """
        Делает уникальным tuple

        :return: [(232, 2818), (232, 2835), (204, 2415)]
        """

        if self.models_list() is not None:
            unique_models = []  # Получаем уникальный id автомобиля
            unique_list_id_models = set(self.models_list())
            for number in unique_list_id_models:  # Проверим, что все значения списка уникальные
                unique_models.append(number)
            return unique_models
        else:
            return None

    def brand_models(self):
        """
        Вернет: list(tuple) или int
        list(tuple) - означает что был запрос по марке и модели либо по модели
        int - Говорит о том, что в запросе есть только марка тачки

        :return: [(232, 2834), (232, 2818)] or 232
        """

        brand = self.brand()
        model = self.models_unique_list()

        def models(brand):
            """
            По бренду вычисляет модели
            Может вернуть пустой список!!!

            :param brand: id тачки
            :return: [(232, 2834), (232, 2818)]
            """
            models = []
            for i in model:
                if i[0] == brand:
                    models.append(i)

            if len(models) >= 1:
                return models
            else:
                return None

        if (brand is not None) and (model is not None):
            model_ = models(brand)
            if model_ is not None:
                return models(brand)
            else:
                return brand

        elif (brand is not None) and (model is None):
            return brand

        elif (brand is None) and (model is not None):
            id_brands = []  # [232, 232, 204, 232]
            for i in model:
                id_brands.append(i[0])

            def count_max():
                d = []  # 3 3 3 1
                for v in id_brands:
                    d.append(id_brands.count(v))
                return d

            def index_max():
                count_m = count_max()
                for b in count_m:  # найдем максимум и отдаст его индекс = 3
                    if max(count_m) == b:
                        return count_m.index(max(count_m))

            def brend_model():
                """
                Выбирает популярные модели по бренду

                :return: [(229, 2761), (229, 2760)]
                """
                if id_brands[index_max()]:
                    return models(id_brands[index_max()])

            return brend_model()

    def dictionary_car(self):
        brand_models = self.brand_models()
        if type(brand_models) == int:
            return dict(brand_id=brand_models, model_id=None)

        elif type(brand_models) == list and len(brand_models) >= 1:
            list_brand = list()
            list_models = list()

            for i in brand_models:
                list_brand.append(i[0])
                list_models.append(i[1])

            data = {
                'brand_id': list_brand[0],
                'model_id': list_models
            }
            return data

        else:
            return dict(brand_id=None, model_id=None)

    def handler(self):
        return self.dictionary_car()
