#coding utf-8
# 1.3
first_tuple = (int(input("часы =")), int(input("минуты = ")), int(input("секунды = ")))
if first_tuple [0]>23:
    print ("ошибка")
elif first_tuple [1]>59:
    print ("ошибка")
elif first_tuple [2]>59:
    print ("ошибка")
second_tuple = (int(input("часы =")), int(input("минуты = ")), int(input("секунды = ")))
if second_tuple [0]>23:
    print ("ошибка")
elif second_tuple [1]>59:
    print ("ошибка")
elif second_tuple [2]>59:
    print ("ошибка")
if first_tuple > second_tuple:
    print ("ошибка")
else:
    print ((second_tuple [0]*360 +second_tuple[1]*60 + second_tuple[2])- (first_tuple[0]*360 +first_tuple[1]*60 +first_tuple[2]))