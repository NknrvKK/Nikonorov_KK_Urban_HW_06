# """
# Задача "Съедобное, несъедобное"____V1:
# Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
# Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?
# Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.
# """
# class Animal:
#
#     def __init__(self, name_an):
#         self.name_an = name_an
#         self.alive = True
#         self.fed = False
#
#     def eat(self, food):
#         self.food = Plant
#         if food.edible:
#             print(f"{self.name_an} съел {food.name_pl}")
#             self.fed = True
#         else:
#             print(f"{self.name_an} не стал есть {food.name_pl}")
#             self.alive = False
#
# class Plant:
#
#     def __init__(self, name_pl):
#         self.edible = False
#         self.name_pl = name_pl
#
# class Mammal(Animal):
#     pass
#
# class Predator(Animal):
#     pass
#
# class Flower(Plant):
#     pass
#
# class Fruit(Plant):
#     def __init__(self, name_pl):
#         super().__init__(name_pl)
#         self.edible = True
#
# #_______ВЫПОЛНЯЕМЫЙ КОД(ДЛЯ ПРОВЕРКИ)__________:
#
# a1 = Predator('Волк с Уолл-Стрит')
# a2 = Mammal('Хатико')
# p1 = Flower('Цветик семицветик')
# p2 = Fruit('Заводной апельсин')
#
# print(a1.name_an)
# print(p1.name_pl)
#
# print(a1.alive)
# print(a2.fed)
# a1.eat(p1)
# a2.eat(p2)
# print(a1.alive)
# print(a2.fed)


"""
Задача "Съедобное, несъедобное"___V2:
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?
Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.
"""
class Animal:
    '''
    Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
    name - индивидуальное название каждого животного.
    '''
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name
        #self.food = Plant

class Plant:
    ''' Для класса Plant атрибут edible = False(съедобность),
    name - индивидуальное название каждого растения'''
    edible = False
    def __init_