__author__ = "Подкопалов"

import random
import numpy as np

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
	"""счетчик условия для lab6 """
	s=0
	for b in a:
		if pred(b):
			s+=1
	return s

def create_matr(row:int,col:int):
	""" создает матрицу вещественных чисел"""
	a= np.random.uniform(0,100,(row,col))
	return a

def print_matrf(a):
	"""выводит матрицу с 2 знаками после ,"""
	print(" матрица :\n")
	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			print(f"{a[i][j]:.2f}",end=" ")
		print("\n",end="")
	print("\n")

def count_if2(a):
	""" создает новую матрицу на основе матрицы а по приципу:
	 https://ivtipm.github.io/Programming/Glava20/index20.htm#z677 """
	b= np.zeros((a.shape[0],a.shape[1]))
	for i in range (a.shape[0]):
		for j in range(a.shape[1]):
			b[i][j]= a[i:a.shape[0],:j+1].sum() 

	"""Numpy.shape в Python: кортеж формы массива.
— это свойство Numpy, которое возвращает кортеж размерности массива."""
	return b