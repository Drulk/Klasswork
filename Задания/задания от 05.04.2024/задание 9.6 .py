#coding utf-8
# задание 9
num = int(input("Введите число = "))
if  (num%7==0 or num%17==0) and (1000<=num<=9999):
    print ("YES")
else:
    print("NO")