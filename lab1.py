__author__ = "Подкопалов"
from math import *

def resist( r1,r2,r3 ):
   return r1*r2*r3 / (r1+r2+r3)

print("Три сопротивления R1, R2, R3 соединены параллельно. Найти сопротивление соединения")

print("Введите сопротивления:")
r1, r2, r3 = list(map(int, input().split()))

print("Сопротивление равно:")
assert resist(2,4,6) - 4 < 1e-8 
print("R = :", resist(r1,r2,r3))
