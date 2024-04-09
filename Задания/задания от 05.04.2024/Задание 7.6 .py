#coding utf-8
# задание 7
age = int(input("Введите возраст пользователя = "))
if age<=13:
    print ("детство")
elif 14<=age<=24:
    print("Молодость")
elif 25<=age<=59:
    print("Зрелость")
else:
    print("Старость")