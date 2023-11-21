__author__ = "Подкопалов"

import my_module as mm
import math
import numpy as np

row =int(input("\nВведите количество строк матрицы: "))
col =int(input("Введите количество столбцов матрицы: "))

a= np.random.uniform(0,100,(row,col))
mm.print_matrf(a)
b=mm.count_if2(a)
mm.print_matrf(b)