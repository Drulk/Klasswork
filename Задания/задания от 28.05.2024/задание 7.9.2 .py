#coding utf-8
# задание 7
a=int(input("введите число:"))
n=1
s=1/n
while s<a:
    print(n,s)
    n+=1
    s+=1/n
