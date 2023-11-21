__author__ = "Подкопалов"
from math import *

print("Даны действительные числа a, b, c. Удвоить эти числа, если a ≥ b ≥ c, и заменить их абсолютными значениями, если это не так.")
a, b, c = list(map(float, input().split()))

if(a>=b>=c):
   a*=2
   b*=2
   c*=2
else:
   a=abs(a)
   b=abs(b)
   c=abs(c)

print(f"a: {a:5.2f}")
print(f"b: {b:5.2f}")
print(f"c: {c:5.2f}")