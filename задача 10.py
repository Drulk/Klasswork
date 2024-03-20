#coding: utf-8
#задача №10
a = int(input("Введите a = "))
c = int(input("Введите c = "))
h = int(input("Введите h = "))
b = (((c-a)/2)**2+h**2)**0.5
p = b*2+a+c
print ("p = " , p)