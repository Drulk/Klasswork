#coding utf-8
#задание 15
m = int(input("введите массу первого материала "))
v = int(input("введите объем первого материала "))
M = int(input("введите массу второго материала "))
V = int(input("введите объем второго материала "))
p = m/v
P = M/V
if p>P:
    print("плотность первого больше")
else:
    print("плотность второго больше")