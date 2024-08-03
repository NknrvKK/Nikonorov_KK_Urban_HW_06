# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче
# "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Горский', 18)
# h1.go_to(5)
h2 = House('Домик в деревне', 2)
# h2.go_to(10)
print(str(h1)) # Название: ЖК Горский, кол-во этажей: 18
print(str(h2)) # Название: Домик в деревне, кол-во этажей: 2
print(len(h1), len(h2)) # 18 2

