#coding utf-8
#Задание 4
A = int(input("Введите высоту шкафа = "))
if 1>A or A>100:
    print("eror")
B = int(input("Введите длину шкафа = "))
if 1>B or B>100:
    print("eror")
C = int(input("Введите ширину шкафа = "))
if 1>C or C>100:
    print("eror")
X = int(input("Введите высоту дверного проёма = "))
if 1>X or X>100:
    print("eror")
Y = int(input("Введите ширину дверного проёмя = "))
if 1>Y or Y>100:
    print("eror")
if ((X>A) and (Y>C)) or ((X>C) and (Y>B)) or ((X>B) and (Y>A)) or ((X>A) and (Y>B)) or ((X>B) or (Y>C)) or ((X>C) and (Y>A)):
    print("YES")
else:
    print("NO")
