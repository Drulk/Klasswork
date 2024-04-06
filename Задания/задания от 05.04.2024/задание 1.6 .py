#coding utf-8
# задание 1
psw = str(input("Введите Пароль:"))
psw2 = str(input("Подтвердите пароль:"))
if psw==psw2:
    print("Пароль принят")
else:
    print("Пароль не принят")