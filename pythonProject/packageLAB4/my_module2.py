from math import sqrt
import datetime

def dev(num1,num2):  # Функция 1

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Это не число")
    if (type(num1) == float and type(num2) == float):
        return num1/num2
    else:
        return



