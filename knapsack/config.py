from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    name: str
    weight: int
    value: int


ITEMS = [
    Item('Карта', weight=9, value=150),
    Item('Компас', weight=13, value=35),
    Item('Вода', weight=153, value=200),
    Item('Сэндвич', weight=50, value=160),
    Item('Глюкоза', weight=15, value=60),
    Item('Кружка', weight=68, value=45),
    Item('Банан', weight=27, value=60),
    Item('Яблоко', weight=39, value=40),
    Item('Сыр', weight=23, value=30),
    Item('Пиво', weight=52, value=10),
    Item('Крем от загара', weight=11, value=70),
    Item('Камера', weight=32, value=30),
    Item('Футболка', weight=24, value=15),
    Item('Брюки', weight=48, value=10),
    Item('Зонтик', weight=73, value=40),
    Item('Непромокаемые штаны', weight=42, value=70),
    Item('Непромокаемый плащ', weight=43, value=75),
    Item('Бумажник', weight=22, value=80),
    Item('Солнечные очки', weight=7, value=20),
    Item('Полотенце', weight=18, value=12),
    Item('Носки', weight=4, value=50),
    Item('Книга', weight=30, value=10),
]

MAX_WEIGHT = 400
