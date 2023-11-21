__author__ = "Подкопалов"

import math 
import matplotlib.pyplot as plt
import numpy as np 

# np.arange создаёт массив от start до stop элементов с указаным шагом step
x = np.arange(0,100,0.1)
#тыща элементов в x типа данных np.array
# создаёт лист из элементов x**2
# применяет векторную операцию синус к каждому элементу массива х типа np.array
y = np.sin(x) * x/100
#y тоже массив типа np.array
# применяет векторную операцию для сложения типа np.array
y1 = y + np.random.uniform(-0.1,0.1,1000) 
# название графика
plt.title("Пример")
# подпись x оси
plt.xlabel("Ось X")
# подпись y оси
plt.ylabel("Ось Y")
# вывод графика с задаными координатами и навзанием cos(x)*x
plt.plot(x,y, label = 'sin(x)*x/100')
# вывод графика с задаными координатами и названием noise alpha - прозрачность графика
plt.plot(x, y1, label = 'sin(x)*x/100 + noise', alpha = 0.5)
# вывод сетки на экран
plt.grid(True)
# вывод названий графиков
plt.legend()
plt.show()