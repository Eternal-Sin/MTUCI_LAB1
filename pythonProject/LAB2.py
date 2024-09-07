
def greet(name): #Функция 1
    print("Приветствую, ",name,"!")

def square(number): #Функция 2
    
    try:
        number = int(number)
    except ValueError:
        print("Это не десятичное число")
    if(type(number)==int):
        return number**2
    else:
        return square(input("Введите десятичное число: "))
    
def set_nums(x,y): #Функция 3.1
    x,y=input("Введите 2 десятичных числа через пробел: ").split()
    print(max_of_two(x,y))

def max_of_two(x,y): #Функция 3.2
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Это не десятичное число")
    if(type(x)==int and type(y)==int):
        return max(x,y)

    else:
        return set_nums(x,y)

def if_prime(number):
    x = 0
    try:
        number = int(number)
    except ValueError:
        print("Это не десятичное число")
    if(type(number)==int):
        for i in range(number):
            if (number%(i+1) == 0):
                x+=1
        if(x==2):
            print("True")
        else:
            print("False")
    else:
        return if_prime(input("Введите десятичное число: "))

"""
greet(str(input("Введите имя: ")))
"""
"""
print(square(input("Введите десятичное число: ")))
"""
"""
set_nums(0,0)
"""
print(if_prime(input("Введите десятичное число: ")))
