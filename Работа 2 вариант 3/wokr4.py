import random
import numpy as np

def func(count,num):
    mat=np.zeros((count,num))
    s=np.zeros(count)
    for i in range(count):
        for j in range(num):
            mat[i,j]=100*random.random()
            s[i]+=mat[i,j]
    print("Все массивы")
    print(mat)
    print()
    x=s.argmax()

    print(mat[x,:]," наибольшая сумма массива - ", s[x])

print("Введите количество массивов: ")
mas = input()
print("Введите количество элементов в массиве: ")
col = input()

func(int(mas), int(col))
