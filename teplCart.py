__aftor__="Подкопалов"           #Работу выполнил 
import numpy as np
import matplotlib.pyplot as plt

#создание рандомной матрицы 
matr = np.random.randint(low=0, high=100, size=(10, 10))
print(matr)
plt.imshow(matr, cmap='hot', interpolation='nearest')                                                   
plt.colorbar()  #добавление цветовой панели
plt.show()      #отображение графика 
