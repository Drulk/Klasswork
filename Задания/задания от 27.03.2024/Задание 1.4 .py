#coding utf-8
# задание 1
A = int(input("число A = "))
if abs(A) > 10000:
    print("Eror")
B = int(input("число B = "))
if abs(B) > 10000:
    print("Eror")
C = int(input("число C = "))
if abs(C) > 10000:
    print("Eror")
if (A%2==0 or B%2==0 or C%2==0) and (A%2==1 or B%2==1 or C%2==1):
    print("YES")
else:
    print("NO")