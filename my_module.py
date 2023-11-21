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


"""----------------- Работа с матрицами --------------------------------------------------"""

def create_matr(row:int,col:int):
	""" создает матрицу вещественных чисел"""
	a= np.random.uniform(0,100,(row,col))
	return a

def print_matrf(a):
	"""выводит матрицу с 2 знаками после ,"""
	print("матрица :\n")
	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			print(f"{a[i][j]:.2f}",end=" ")
		print("\n",end="")
	print("\n")

def count_if2(a):
	""" создает новую мтарицу на основе матрицы а по приципу:
	 https://ivtipm.github.io/Programming/Glava20/index20.htm#z677 """
	b= np.zeros((a.shape[0],a.shape[1]))
	for i in range (a.shape[0]):
		for j in range(a.shape[1]):
			b[i][j]= a[i:a.shape[0],:j+1].sum()
	return b

def mult_matr_list(matr:list,matr2:list):
 	res = [[random.randrange(0,100) for j in range(len(matr2[0]))] for i in range(len(matr))]
 	for i in range(len(matr)):
 		for j in range(len(matr2[0])):
 			for k in range(len(matr2)):
 				res[i][j]+= matr[i][k]*matr2[k][j]
 	return res

"""-------------------------------yield-------------------------------------- """

def crm(n: int ):
	""" генератор , который генерирует только (-1)**(i+1)/i"""
	for i in  range(1,n+1):
		yield ((-1)**(i+1))/i

def crm2(n: int ):
	"""генератор, который генерирует последовательные элементы с сохранением предыдущего """
	temp2=0
	for i in  range(1,n+1):
		temp2+=((-1)**(i+1))/i
		yield temp2


"""------------------------------ Конец -------------------------------------"""
