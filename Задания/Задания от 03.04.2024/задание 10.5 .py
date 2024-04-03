#coding utf-8
# задание 10
P=int(input("Введите пробег:"))
D=int(input("Введите сегодняшнее число:"))
cp=P
sp=0
while cp!=0:
    sp+=cp%10
    cp//=10
if sp>D:
    print("Сброс")
    print("Пробег:", 0)
else:
    print("Сегодня не сломался")
    print("Пробег:", P)