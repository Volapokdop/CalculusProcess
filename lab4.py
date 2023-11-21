__author__ = "Подкопалов"

print("Дано натуральное число n. Вычислить: k=1 -> n, 1/k")
n=int(input())

s = float(0)
for k in range(1, n+1):
    s += 1/k
print(f'Сумма ряда равна ={s:6.2f}')