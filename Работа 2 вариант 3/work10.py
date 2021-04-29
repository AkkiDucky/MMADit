import random
import numpy as np


def minmax(m):
    mas=np.zeros(m)
    for i in range(m):
        mas[i]=random.random()*100
    print(mas," - полученный массив")
    min = np.min(mas)
    max = np.max(mas)
    a =list()
    a.append(min)
    a.append(max)
    b=tuple(a)
    print(b)

print("Введите количетсво элементов массива:")
m = int(input())

minmax(m)
