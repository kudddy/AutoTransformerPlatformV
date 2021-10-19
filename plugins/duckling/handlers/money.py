import re


class TextMoney:

    def __init__(self, text):
        self.text_list = text  # Текст пользователя str
        self.digit = re.compile(r'\d+')
        self.pattern = re.compile(
            r'((?:за\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s))|'  # 1 from to
            r'((?:от\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s[^года]))|'  # 2 from
            r'((?:до\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s[^года]))|'  # 3 to
            r'((?:не\s?дешевле\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s))|'  # 4 from
            r'((?:не\s?дороже\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s))|'  # 5 to
            r'((?:дороже\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s))|'  # 6 from
            r'((?:дешевле\s*\d\s?)(?:\d*\s?\d*\s?)(?:К\w*|к\w*|₽|$|\s))|'  # 7 to
            r'((?:от\s*(?:\d{2}|\d{3})\s*)(?:(?=до)))')  # 8 from

    def get_money(self):
        regex = self.pattern.finditer(self.text_list)
        price_from = None
        price_to = None

        for item in regex:
            for i in range(1, 9):
                if item.group(i):
                    money_replace = self.digit.search(item.group(i).replace(' ', ''))
                    money = int(money_replace.group())
                    if i == 1:
                        if money < 1000:
                            price_from = int(str(money) + '000')
                            price_to = (int(str(money) + '000'))  # + 49000 Добавляем?
                        else:
                            price_from = money
                            price_to = money  # + 49000 Добавляем?
                    elif i in [2, 4, 6]:
                        if money < 1000:
                            price_from = int(str(money) + '000')
                        else:
                            price_from = money
                    elif i in [3, 5, 7]:
                        if money < 1000:
                            price_to = int(str(money) + '000')
                        else:
                            price_to = money
                    elif i == 8:
                        price_from = int(str(money) + '000')

        return dict(price_from=price_from, price_to=price_to)

    def handler(self):
        return self.get_money()
