#coding utf-8
#задание 1
a = int(input("Введите натуральное число a = "))
b = int(input("Введите натуральное число b = "))
c = int(input("Введите натуральное число c = "))
if a+b>c:
    print ("Yes")
elif a+c>b:
    print ("Yes")
elif c+b>a:
    print ("Yes")
else:
    print ("No")
