#coding utf-8
# задание 8
x=int(input("кубик Кости = "))
y=int(input("кубик Владельца= "))
if x>=y:
    рез=x-y
    print(рез,"\nКостя платит")
else:
    рез=x+y
    print (рез, "\nВладелец платит")
print ("Игра окончена")