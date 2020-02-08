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
print(type(frac))
print(frac)

# số phức
comp    =   complex(2,5)
print(type(comp))
# lấy ra phần thực
print(comp.real)
# lấy ra phần ảo
print(comp.imag)
print(2**3)