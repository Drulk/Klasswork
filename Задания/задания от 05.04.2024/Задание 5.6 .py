#coding utf-8
# задание 5
num1 = int(input("Введите первое число = "))
num2 = int(input("Введите второе число = "))
num3 = int(input("Введите третье число = "))
n=3
d=num2-num1
if (num1+d*(n-1))==num3:
    print("Yes")
else:
    print("No")