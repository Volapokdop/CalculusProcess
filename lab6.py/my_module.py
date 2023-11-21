__author__ = "Подкопалов"

import random
import numpy

def create_mass_double(n:int):
	"""создание случайного массива дробных чисел """
	a=[random.uniform(0,100) for i in range(1,n+1)]  #генератор списка

	# for i in range(1,n+1):
	# 	a[i]= random.uniform(0,100)
	return a

def print_masf(a):
	""" выводит массив с 2 знаками после , """
	print("массив: ",end=" ")
	for b in a:
		print(f"{b:.2f}",end=" ")


def create_mass_int(n:int):
	"""создание случайного массива целых чисел """
	a=[random.randint(0,100) for i in range(1,n+1)]  #генератор списка

	# for i in range(1,n+1):
	# 	a[i]= random.uniform(0,100)
	return a

def calc_f1(a,n:int):
	""" вычисление суммы ряда lab5"""
	factorial=1
	s=0
	for i in range(0,n):
		if i==0:
			factorial=1
		else:
			factorial*=i
		s+=a[i]/factorial
	return s

def count_if(a,pred): 
	"""счетчик условия для lab6 
	a - массив данных, получаемых из основной программы
	pred - функция, возвращающая результат логического уравнения pred
    return - счётчик чисел, удовлетворяющих условию
	"""
	s=0
	for b in a:
		if pred(b):
			s+=1
	return s  