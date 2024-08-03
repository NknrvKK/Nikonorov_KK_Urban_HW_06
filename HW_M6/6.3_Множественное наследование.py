# """__________Задача "Мифическое наследование"_V1 (в каждом классе в
# конструкторе присутсвует метод super().__init__(*args), потому в наследственном классе тоже просто
#                           super().__init__(*args):__________"""
# class Horse:
#     def __init__(self, *args):
#         self.x_distance = 0
#         self.sound = 'Frrr'
#         super().__init__(*args)
#     def run(self, dx):
#        self.x_distance += dx
#
#
# class Eagle:
#     def __init__(self, *args):
#         self.y_distance = 0
#         self.sound = 'I train, eat, sleep, and repeat'
#         super().__init__(*args)
#
#     def fly(self, dy):
#         self.y_distance += dy
#
#
# class Pegasus(Horse, Eagle):
#     def __init__(self, *args):
#         super().__init__(*args)
#
#     def move(self, dx, dy):
#         self.run(dx)
#         self.fly(dy)
#
#     def get_pos(self):
#         return self.x_distance, self.y_distance
#
#     def voice(self):
#         print(self.sound)
#
# ### ____ВЫПОЛНЯЕМЫЙ КОД(ДЛЯ ПРОВЕРКИ)_____:
#
# p1 = Pegasus()
#
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()


"""__________Задача "Мифическое наследование_V2"(в родит классах нет метода super().__init__(*args):,
# потому в конструкторе дочернего класса будут прямые ссылки на родит классы__________"""
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
       self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

### ____ВЫПОЛНЯЕМЫЙ КОД(ДЛЯ ПРОВЕРКИ)_____:

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


