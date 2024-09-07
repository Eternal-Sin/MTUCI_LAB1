
def greet(name):
    print("Приветствую, ",name,"!")

def square(number):
    
    try:
        number = int(number)
    except ValueError:
        print("Это не число")
    if(type(number)==int):
        return number**2
    else:
        return square(input("Введите ЧИСЛО: "))
greet(str(input("Введите имя: ")))


print(square(input("Введите число: ")))

