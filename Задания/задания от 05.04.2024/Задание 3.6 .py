#coding utf-8
# задание 3
num = str(input("Введите число = "))
x=(int(num[0])+ int(num[3]))
y=(int(num[1])-int(num[2]))
if x==y:
    print("ДА")
else:
    print("Нет")