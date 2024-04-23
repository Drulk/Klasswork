#coding utf-8
# задание 8
month=int(input("введите номер месяца:"))
if 3<=month<6:
    print("Весна")
elif 6<=month<9:
    print("Лето")
elif 9<=month<12:
    print("Осень")
else:
    print("Зима")