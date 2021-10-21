from datetime import datetime
import re


class TextYear:

    def __init__(self, text):
        self.text_list = text  # Текст пользователя str
        self.now = datetime.now()
        self.digit = re.compile(r'\d+')
        self.pattern = re.compile(
            r'((?:от|с)\s*(?:\d{4}|\d+\s*год\w*))|'
            r'((?:до|по)\s*(?:\d{4}|\d+\s*год\w*))|'
            r'((?:\d+\s*год\w*)|(?:год\w*\s*\d+))|'
            r'((?:старше|не\s*моложе)\s*\d+\s*(?:год\w*|лет))|'
            r'((?:моложе|не\s*старше)\s*\d+\s*(?:год\w*|лет))')

    def get_date(self):
        regex = self.pattern.finditer(self.text_list)
        date_from = None
        date_to = None
        for item in regex:
            for i in range(1, 6):
                if item.group(i):
                    date = int(self.digit.search(item.group(i)).group())
                    if i == 3:
                        if 1900 < date <= self.now.year:
                            date_from = date
                            date_to = date
                        elif 1 <= date <= self.now.year - 2000:
                            date_from = date + 2000
                            date_to = date + 2000
                        else:
                            date_from = date + 1900
                            date_to = date + 1900
                    elif i in [1, 5]:
                        if 1900 < date <= self.now.year:
                            date_from = date
                        elif 1 <= date <= self.now.year - 2000:
                            date_from = self.now.year - date if i == 5 else date + 2000
                        else:
                            date_from = self.now.year - date if i == 5 else date + 1900
                    else:
                        if 1900 < date <= self.now.year:
                            date_to = date
                        elif 1 <= date <= self.now.year - 2000:
                            date_to = self.now.year - date if i == 4 else date + 2000
                        else:
                            date_to = self.now.year - date if i == 4 else date + 1900

        return dict(year_from=date_from, year_to=date_to)

    def handler(self):
        return self.get_date()
