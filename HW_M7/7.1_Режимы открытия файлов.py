# class Product:
#     def __init__(self, name: str, weight: float, category: str):
#         self.name = name,
#         self.weight = weight,
#         self.category = category
#
#     def __str__(self):
#         return f'{self.name}, {self.weight}, {self.category}'
#
#
# class Shop(Product):
#     def __init__(self, name, weight, category, __file_name = 'products.txt'):
#         super().__init__(name, weight, category)
#         self.__file_name = __file_name
#     def get_products(self):
#         info_from_file_txt = open(self.__file_name, 'r')  # Создали файли, кот. просто его открывает в коде
#         file_str = info_from_file_txt.read()          # Создали строковый файл текста открытого файла
#         info_from_file_txt.close()                        # Закрыли открытый исходный файл
#         print(file_str)                           # Напечатали текстовый полученный файл
#     def add(self, *products):
#         for prod in products:
#             prod_s = str(prod)
#             info_from_file_txt = open(self.__file_name, 'r')
#             file_str = info_from_file_txt.read()  # Создали строковый файл текста открытого файла
#             info_from_file_txt.close()
#             if prod_s in file_str:
#                 print(f'Продукт {prod_s} уже есть в магазине')
#             else:
#                 info_from_file_txt = open(self.__file_name, 'a') # добавляем в нашу строку новый продукт
#                 info_from_file_txt.write(prod_s)
#                 info_from_file_txt.close()
#
#
# s1 = Shop('', 0, '')
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
#
# print(p1)
# print(p2)
# print(p3)  # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())

from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        for product_1 in products:
            if product_1.name in self.get_products():
                print(f'Продукт {product_1.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(product_1.__str__() + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

s1.get_products()



