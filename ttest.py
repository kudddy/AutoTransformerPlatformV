class SberAutoLoader:
    def __init__(self, long: int, short: int):
        self.long = long
        self.short = short


class SberAutoProcessor(SberAutoLoader):
    def __init__(self, long, short):
        super().__init__(long, short)

    def get(self):
        return self.long


lol = SberAutoProcessor(long=2, short=2)

print(lol.long)

print(lol.get())




