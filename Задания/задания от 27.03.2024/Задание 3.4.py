#coding utf-8
#Задание 3
a = int(input("введите первое число"))
b = int(input("введите второе число"))
c = int(input("введите третье число"))
if a>b:
    (a,b)=(b,a)
if b>c:
    (b,c)=(c,b)
if a>b:
    (a,b)=(b,a)
print (a,b,c)