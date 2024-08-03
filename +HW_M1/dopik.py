class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

comedy = Comedian("Kir", 'Nik', 12)
print(comedy)


# Метод .format позволяет вставлять в строку любой формат
price = '1, 2, 3, 4'
price1 = (1, 2, 3, 4)
price2 = {'1, 2': 3}
price3 = 'ASDFG'
txt = "The price is {} dollars"
print(txt.format(price))
print(txt.format(price1))
print(txt.format(price2))
print(txt.format(price3))