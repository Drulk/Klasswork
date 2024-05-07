#coding utf-8
# задание 9
x=int(input("введите первое число:"))
y=int(input("введите второе число:"))
if x>y:
    x=x-y
    print(x)
elif y>x:
    y=y-x
    print(y)