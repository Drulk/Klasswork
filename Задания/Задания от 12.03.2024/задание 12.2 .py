#coding utf-8
#задание 12
a = int(input("введите сторону квадрата "))
r = int(input("введите радиус круга "))
p = 3.14
m = p*r**2
n = a**2
if m>n:
    print("площадь круга больше")
else:
    print("площадь квадрата больше")