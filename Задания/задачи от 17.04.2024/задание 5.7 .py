#coding utf-8
# задание 5
x1=int(input("введите номер строки ладьи:"))
y1=int(input("введите номер столбца ладьи:"))
x2=int(input("введите номер строки другой фигуры:"))
y2=int(input("введите номер столбца другой фигуры:"))
if x1==x2 or y1==y2:
    print("YES")
elif x1==x2 and y1==y2:
    print("NO")
else:
    print("NO")