#coding utf-8
# задание 7
x=int(input("введите координаты точки :"))
y=int(input("введите координаты точки :"))
if x>0 and y>0:
    print("первый квадрант")
elif x<0 and y>0:
    print("второй квадрант")
elif x<0 and y<0:
    print("третий квадрант")
elif x>0 and y<0:
    print("четвёртый квадрант")