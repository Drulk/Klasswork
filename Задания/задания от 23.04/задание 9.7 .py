#coding utf-8
# задание 9
c=int(input("введите текущую температуру:"))
if 10<=c:
    print("летняя одежда")
elif 0<=c:
    print("осенняя одежда")
else:
    print("зимняя одежда")