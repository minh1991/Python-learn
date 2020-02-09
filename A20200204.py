msg= "hello world"
print(msg)

# test command

num_1   =   2020
num_2   =   1000
num_3   =   3.14
num_4   =   2.90578348975483957435634875628734365345634573475934759345043258
# print(num_1 + num_2)
a = type(num_4)
# print(num_4)
from decimal import *

# print(Decimal(num_4))

# tạo ra một phân số
from fractions import *
frac    =   Fraction(6,9)
# print(type(frac))
# print(frac)

# số phức
comp    =   complex(2,5)
print(type(comp))
# lấy ra phần thực
print(comp.real)
# lấy ra phần ảo
# print(comp.imag)
# print(2**3)

# 20200208
# print("Obama",end=' ')
# print("Xin chào",end=' ')
# print("Putin")

# print(end='Mời bạn nhập 1 số:')
# a=input()
# print('số bạn vừa nhập = ',a)

# phép nhân chuỗi
# strA    =   "hello boy \n"
# strB    =   strA * 5
# print(strB)





# strC    =   strB in strA


str1    = int("66")
str2    = str1 + 10
str3    = 60
str4    = str(str3) + "10"
# print(str4,type(str3), type(str4))


strA    =   'My name is %s %s  ' %('Lee', 'NUM')
print(strA)

strC    = 'một số bất kỳ là : %.2f '  %(15.888)
print(strC)

strD    =   'hiển thị: %r'  %('tôi')
print(strD)

strE    =   'abcXYZ'
strA    =   f'vấn đề là  {strE}'
print(strA)

strF    =   'a:{tmp1} b:{tmp2} c:{tmp3}'
strR    =   strF.format(tmp1="what", tmp2=5,tmp3="men")
print(strR)