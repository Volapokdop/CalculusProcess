__aftor__="Подкопалов"           #Работу выполнил 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
#создание рандомного массива 
matr = np.random.randint(low=1, high=10, size=(5, 5)) #low - мин занч   high - макс знач  size- размерность 
print(matr) #выводим матрицу 
#превратить матрицу в массив
arr = matr.flatten() #сглаживаем матрицу в одн-й массив с помощью метода flatten и печатаем массив 
print(arr)
#построение гистограммы
sns.histplot(arr) #создаем гистограмму
plt.title('Гистограмма') #Название гистограммы 
plt.xlabel("Диапазон")
plt.ylabel("Кол-во значений")
plt.show()  #выводим гистограмму 

#гистограмма отображает частоту появления каждого значения в массиве
#ось x представляет диапазон значений в массиве, ось y частоту появления каждого значения в этом диапазоне

