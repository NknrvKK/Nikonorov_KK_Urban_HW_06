"""
________Задача "Некорректность":___________
Создайте 3 класса (2 ИЗ КОТОРЫХ БУДУТ ИСКЛЮЧЕНИЯМИ):
              !!!!________________________________!!!!
"""
class IncorrectVinNumber(Exception):

  def __init__(self, message):
    self.message = message


class IncorrectCarNumbers(Exception):

  def __init__(self, message):
    self.message = message


class Car:

  def __init__(self, model: str, vin: int, numbers: str):
    """Атрибут объекта model - название автомобиля (строка)
       Атрибут объекта __vin - vin номер автомобиля (целое число).
          Уровень доступа private
       Атрибут __numbers - номера автомобиля (строка)"""
    self.model = model
    if self.__is_valid_vin(vin):
      self.__vin = vin
    if self.__is_valid_numbers(numbers):
      self.__numbers = numbers

  def __is_valid_vin(self, vin):
    if not isinstance(vin, int) == True:
      raise IncorrectVinNumber('Некорректный тип vin номер')
    if  not (1000000 <= vin <= 9999999):
      raise IncorrectVinNumber('Неверный диапазон для vin номера')
    else:
      return True

  def __is_valid_numbers(self, numbers):
    if not isinstance(numbers, str) == True:
      raise IncorrectCarNumbers('Некорректный тип данных для номеров')
    if len(numbers) != 6:
      raise IncorrectCarNumbers('Неверная длина номера')
    else:
      return True


###______Пример выполняемого кода:___________________________________________________________
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')