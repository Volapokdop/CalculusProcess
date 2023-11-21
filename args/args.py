__author__ = "Подкопалов"

import my_module as mm
import sys

# записываем аргументы в переменую args [1:] - с 1 до последней
args = sys.argv[1:]

print(args)

# # match - улучшенный аналог switch c++ поддерживает разные типы данных
# match - сопоставление с образцом
match args:
    # случай если ничего не было передано
    case []:
    	print("программа запущена без аргументов")
    	n=int(input("Введите длину массива : "))
    	a=mm.create_mass_double(n)
    	mm.print_masf(a)
    	print(f"\nРезультат: {mm.calc_f1(a,n):.2f}")
        # случай если было введено help
    case ['--help']:
        print("справка: введите массив для выполнения суммирования по формуле: a[i]/(i-1)!")
        # случай если был передан размер массива
    case['--length',n]:
    	print("Очень интерено")
    	a=mm.create_mass_double(int(n))
    	mm.print_masf(a)
    	print(f"\nРeзультат: {mm.calc_f1(a,int(n)):.2f}")
    case['--length', *other]:
        print("Неверное число параметров")
    case[*other]:
    	print("Неверно. Ты чего понаписал?")
