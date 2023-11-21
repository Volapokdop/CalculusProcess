__author__ = "Подкопалов"

import numpy as  np 
import my_module as mm 
import random
import time 
import torch

torch.cuda.is_available()

print("Введите длину матрицы (n x m): ")
row= int(input("n: "))
col= int(input("m: "))

""" ----Создание матриц через numpy ----"""
# a= mm.create_matr(row,col)
# b= mm.create_matr(row,col)
a= np.random.uniform(0,100,(row,col))
b= np.random.uniform(0,100,(row,col))
t1= time.time()
c= a@b
t2=time.time()

"""---- создание матриц с помощью листов -----"""
# matr = [[random.randrange(0,100) for j in range(col)] for i in range(row)]
# matr2 = [[random.randrange(0,100) for j in range(col)] for i in range(row)]
# tstart= time.time()
# res= mm.mult_matr_list(matr,matr2)
# tend=time.time()
"""---- создание матрицы при помощи tourch """
"""  по умолчанию переменные - в оперативной памяти(cpu) в торче"""
ta = torch.rand(row, col).cuda()
tb = torch.rand(row, col),cuda()
st = time.time()
tc = torch.mul(ta, tb).cuda()
en = time.time()

print("Время перемножения матриц numpy: ",t2-t1)
# print("Время перемножения матриц list : ",tend-tstart)
print("Время перемножения матриц torch : ",en-st)



""" Введите длину матрицы (n x m):
n: 1000
m: 1000
Время перемножения матриц numpy:  0.0009965896606445312
Время перемножения матриц list :  78.02940034866333
Время перемножения матриц torch :  0.001989126205444336
"""

"""
List - выполняет вычисления дольше , потому что написан на питоне и код интерпритируется
numpy- написан на с++, и работает очень быстро

torch cpu работает медленнее torch cuda  так как на видеокарте больше АЛУ(вычислительных блоков)
 """
# import numpy as  np 
# import random
# import time 
# import torch

# __author__ = "Подкопалов"

# torch.cuda.is_available()

# print("Введите длину матрицы (n x m): ")
# row= int(input("n: "))
# col= int(input("m: "))

# """ ----Создание матриц через numpy ----"""
# # a= mm.create_matr(row,col)
# # b= mm.create_matr(row,col)
# a= np.random.uniform(0,100,(row,col))
# b= np.random.uniform(0,100,(row,col))
# t1= time.time()
# c= a@b
# t2=time.time()

# """---- создание матриц с помощью листов -----"""
# # matr = [[random.randrange(0,100) for j in range(col)] for i in range(row)]
# # matr2 = [[random.randrange(0,100) for j in range(col)] for i in range(row)]
# # tstart= time.time()
# # res= mm.mult_matr_list(matr,matr2)
# # tend=time.time()
# """---- создание матрицы при помощи tourch """
# """  по умолчанию переменные - в оперативной памяти(cpu) в торче"""
# ta = torch.rand(row, col).cuda()
# tb = torch.rand(row, col).cuda()
# st = time.time()
# tc = torch.mul(ta, tb).cuda()
# en = time.time()

# ta = torch.rand(row, col)
# tb = torch.rand(row, col)
# st2 = time.time()
# tc = torch.mul(ta, tb)
# en2 = time.time()

# print("Время перемножения матриц numpy: ",t2-t1)
# # print("Время перемножения матриц list : ",tend-tstart)
# print("Время перемножения матриц torch-cuda : ",en-st)
# print("Время перемножения матриц torch : ",en2-st2)
# print("Время перемножения матриц numpy: ",t2-t1)
# # print("Время перемножения матриц list : ",tend-tstart)
# print("Время перемножения матриц torch-cuda : ",en-st)
# print("Время перемножения матриц torch : ",en2-st2)
# Введите длину матрицы (n x m): 
# n: 10000
# m: 10000
# Время перемножения матриц numpy:  60.48672604560852
# Время перемножения матриц torch-cuda :  0.000995635986328125
# Время перемножения матриц torch :  0.22952938079833984