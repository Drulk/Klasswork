#coding utf-8
# задание 4
x=int(input("введите первый катет треугольника:"))
y=int(input("введите второй катет треугольника:"))
if (x<0 or x>1000) and (y<0 or y>1000):
    print("ошибка")
z= (x**2+y**2)**0.5
print(z)