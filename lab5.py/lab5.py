__author__ = "Подкопалов"

import my_module as mm
import math

n=int(input("Введите длину массива: "))
a=mm.create_mass_double(n)
print("массив: ",end=" ")
mm.print_mass(a)
print(f"\nРезультат: {mm.calc_f1(a,n):.2f}")