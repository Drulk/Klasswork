#coding utf-8
# задание 13
M = int(input("Введите число месяца = "))
if M==2:
    print(28)
elif M==4 or M==6 or M==9 or M==11:
    print(30)
else:
    print(31)