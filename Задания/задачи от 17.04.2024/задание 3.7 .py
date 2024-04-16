#coding utf-8
# задание 3
k=int(input("введите число:"))
s=0
while k!=0:
    s=s+k%10
    k=k//10
print(s)