num1 = 0;
num2 = 0;
biggerNum=0;


num1 = int(input("Введите число: "))
for i in range(num1):
    print(i+1)
#--------------------------------------------
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if(num1>=num2):
    biggerNum = num1
else:
    biggerNum = num2
    
print("Большее: ", biggerNum)
