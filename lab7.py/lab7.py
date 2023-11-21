__author__ = "Подкопалов"

import my_module as mm

print("Дано натуральное число n. Вычислить: k=1 -> n, 1/((k^2)!)")

s = 0

print("Введите число n")
n = int(input())

s = mm.func_sum_7lab(n)
 
print(f"\nСумма массива: {s:.3f}",)