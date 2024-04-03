#coding utf-8
# задание 2
from random import randint
x = randint(1,10)
y = int(input("какое число я загадал?"))
if y==x:
    print("Угадал!")
else:
    print("Не угадал!")
print("Конец игры")