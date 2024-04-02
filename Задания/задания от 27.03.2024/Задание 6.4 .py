#coding utf-8
#Задание 6
A1 = int(input("введите высоту первой коробки"))
if (A1<0 or A1>1000):
    print ("Eror")
B1 = int(input("введите ширину первой коробки"))
if  (B1<0 or B1>1000):
    print ("Eror")
C1 = int(input("введите длину первой коробки"))
if  (C1<0 or C1>1000):
    print ("Eror")
A2 = int(input("введите высоту второй коробки"))
if (A2<0 or A2>1000):
    print ("Eror") 
B2 = int(input("введите ширину второй коробки"))
if  (B2<0 or B2>1000):
    print ("Eror") 
C2 = int(input("введите длину второй коробки"))
if (C2<0 or C2>1000):
    print ("Eror") 
if (A1==A2 or A1==B2 or A1==C2) and (B1==A2 or B1==B2 or B1==C2) and (C1==A2 or C1==B2 or C1==B2):
    print ("Box are equal")
if ((A1*B1*C1)<(A2*B2*C2)):
    print ("first box is smaller than the second one")
if ((A1*B1*C1)>(A2*B2*C2)):
    print ("first box is larger than the second one")
else:
    print ("boxes is incomparable")