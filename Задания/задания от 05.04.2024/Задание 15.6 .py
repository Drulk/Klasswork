#coding utf-8
# задание 15
num1 = int(input("Введите первое число = "))
num2 = int(input("Введите второе число = "))
x=str(input("введите обозначение математической операции:"))
if x=="+":
    print(num1 + num2)
elif x=="-":
    print(num1 - num2)
elif x=="*":
    print(num1 * num2)
elif x=="/":
    if num2==0:
        print("на ноль делить нельзя")
    else:
        print(num1 / num2)
else:
    print("Неверная операция")