#coding utf-8
# задание 2
a1=int(input("введите координату начала:"))
b1=int(input("введите координату конца:"))
a2=int(input("введите координату начала:"))
b2=int(input("введите координату конца:"))
if a1>b1 or a2>b2:
    print("ошибка")
elif b1==a2:
    print(a2)
elif b1>a2:
    print(a2,b1)
elif b1<a2:
    print("пустое множество")