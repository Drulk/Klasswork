#coding utf-8
# задание 7
x=int(input("введите первое число:"))
y=int(input("введите второе число:"))
z=x*y
if z<0:
    z=z*-2
    print(z)
else:
    z=z*3
    print(z)