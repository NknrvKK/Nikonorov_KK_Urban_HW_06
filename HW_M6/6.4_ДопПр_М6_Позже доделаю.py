"""


"""
class Figure:
    sides_count = 0
    def __init__(self, __sides: list, __color: list, filled: bool):
        self.__sides = __sides # Атрибуты(инкапсулированные)
        self.__color = __color # Атрибуты(инкапсулированные) / (список цветов в формате RGB)
        self.filled = filled   # Атрибуты(публичные)

    def get_color(self):
        return self.__color

    def __is_valid_color(self):
        for i in range(len(self.__color)):
            if self.__color[i] in range(0, 256) and type(self.__color[i]) is int:
                self.is_valid_color = True
                print('Цвет задан верно')
            else:
                self.is_valid_color = False
                print('Цвет задан не корректно! Корректный цвет: все значения ',
                      'r, g и b - целые числа в диапазоне от 0 до 255 (включительно)')
                break

    def set_color(self, r, g, b):
        self.set_color = []
        for i in r, g, b:
            if self.is_valid_color:
                self.set_color.append(i)
            else:
                self.set_color = self.__color
        return self.set_color

    def __is_valid_sides(self, *__sides: int):
        if type() = int and > 0
        return a = True

    def get_sides(self):
        return

    def __len__(self):
        return

    def set_sides(self, *new_sides):
        return





# ###_______________Код для проверки:____________________
#
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())

