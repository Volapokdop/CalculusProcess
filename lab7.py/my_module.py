__author__ = "Подкопалов"

import random
import numpy
import math

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

def print_matrf(a,row,col):
	"""выводит матрицу с 2 знаками после ,"""
	for i in range(row+1):
		for j in range(col+1):
			print(f"{a[i][j]:.2f}",end=" ")
	print("\n",end=" ")

def func_sum_7lab(n):
	"""Считает сумму ряда 1/((k^2)!) 1 -> n"""
	s = 0
	for i in range(1,n+1):
	    s += 1/math.factorial(i**2)
	return s