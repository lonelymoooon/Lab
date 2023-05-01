class Human:  # 1
    default_name = 'No name'  # 2
    default_age = 0

    def __init__(self, name=default_name, age=default_age):  # 3
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):  # 4
        print('Name:', self.name)
        print('Age', self.age)
        print('Money:', self.__money)
        print('House:', self.__house)

    @staticmethod  # 5
    def default_info():
        print('Default Name:', Human.default_name)
        print('Default Age:', Human.default_age)

    def __make_deal(self, house, discount):  # 6
        self.__money -= house.final_price(discount)
        self.__house = house

    def earn_money(self, money):  # 7
        self.__money += money

    def buy_house(self, house, discount):  # 8
        if self.__money >= house.final_price(discount):
            self.__make_deal(house, discount)
            print('Successfully')
        else:
            print('Insufficient funds')


class House:  # 9
    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def final_price(self, discount):
        return self.__price * (100 - discount) / 100


class SmallHouse(House):  # 10
    def __init__(self, price):
        super().__init__(40, price)


# Тесты
# 1 вызов справочного метода default_info() для класса Human()
Human.default_info()
# 2 создание объекта для класса Human
pepe = Human('Luci', 27)
# 3 вывод справочной информации о созданном объекте
pepe.info()
# 4 создание объекта класса SmallHouse
box = SmallHouse(10)
# 5 пробуем купить созданный дом-коробку
pepe.buy_house(box, 10)  # дом, скидка
# 6 поправляем финансовое положение
pepe.earn_money(100)
# 7 снова пробуем купить дом-коробку
pepe.buy_house(box, 10)
# 8 смотрим, что поменялось
pepe.info()


