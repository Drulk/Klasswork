#coding utf-8
# задание 12
a = int(input("Введите первое число = "))
b = int(input("Введите второе число = "))
c = int(input("Введите третье число = "))
if a<b<c or c<b<a:
    print(b)
if a<c<b or b<c<a:
    print(c)
if c<a<b or b<a<c:
    print(a)