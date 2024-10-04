from math import sqrt
import datetime

from packageLAB4 import my_module1 , my_module2

def square(number):  # Функция 1

    try:
        number = float(number)
    except ValueError:
        print("Это не число")
    if (type(number) == float):
        return sqrt(number)
    else:
        return square(input("Введите десятичное число: "))



print(square(input("Введите число: ")))
print(datetime.datetime.now())

a, b = input("Введите 2 числа через пробел для суммы: ").split()
print(my_module1.summ(a,b))
a, b = input("Введите 2 числа через пробел для деления: ").split()
print(my_module2.dev(a,b))