__author__ = "Подкопалов"

import my_module as mm
import math

print("Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:")
print("Кратных 3 и не кратные 5")
n=int(input("Введите длину массива: "))

a=mm.create_mass_int(n)
print("\nмассив:",a)
print(f"\nОтвет:",mm.count_if(a,lambda x: x%3==0 and x%5!=0)) #lambda для функции возвращающей результат логического условия