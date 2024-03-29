#coding utf-8
#Задание 5
A = int(input("введите высоту кирпича"))
B = int(input("введите ширину кирпича"))
C = int(input("введите длину кирпича "))
D = int(input("введите высоту отверстия"))
E = int(input("введите ширину отверстия"))
if ((D>A)and(E>B))or((D>A)and(E>C))or((D>B)and(E>A))or((D>B)and(E>C))or((D>C)and(E>B))or((D>C)and(E>A)):
    print ("YES")
else:
    print("NO")