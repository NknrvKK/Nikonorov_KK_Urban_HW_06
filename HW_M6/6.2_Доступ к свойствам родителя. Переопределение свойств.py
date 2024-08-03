"""____________________Задача "Изменять нельзя получать": _______________________"""
class Vehicle:
    __COLOR_VARIANTS = ['RED', 'BLACK', 'WHITE', 'BLUE', 'GREEN']
    """Константные(постоянные) значения в Python принято писать полностью в верхнем 
    регистре (капсом), как в случае списка цветов или количеством пассажиров."""
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner     # владелец транспорта (владелец может меняться)
        self.__model = __model # модель (марка) транспорта (не изменяется)
        self.__engine_power = __engine_power # мощность двигателя (не изменяется)
        self.__color = __color # название цвета (не изменяется)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        str1 = self.get_model()
        str2 = self.get_horsepower()
        str3 = self.get_color()
        print('\n',str1,'\n',str2,'\n',str3,'\n',f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        new_color_update = new_color.lower()
        Vehicle.__COLOR_VARIANTS_update = list(Vehicle.__COLOR_VARIANTS[i].lower() for
                                               i in range(len(Vehicle.__COLOR_VARIANTS)))
        if new_color_update in Vehicle.__COLOR_VARIANTS_update:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()