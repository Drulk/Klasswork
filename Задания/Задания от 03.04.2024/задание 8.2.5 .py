#coding utf-8
# задание 8.2.5
hours=int(input("Введите количество отработанных часов"))
остаток=int(input("Введите остаток по кредиту"))
еда=int(input("Введите количество денег на еду"))
зарплата=((200*hours)/2**3)+hours
if зарплата>=(еда+остаток):
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать!")