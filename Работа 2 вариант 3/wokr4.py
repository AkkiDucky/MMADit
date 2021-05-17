import random
import numpy as np
#4. Написать функцию, которая генерирует несколько массивов случайных чисел и возвращает тот, в котором сумма элементов наибольшая.
#Для генерации случайных чисел используйте функцию random из модуля random. Модуль random необходимо предварительно подключить с помощью команды import random.
#Для вычисления суммы элементов массива используйте встроенную функцию sum.
#Функция принимает 2 параметра: количество генерируемых массивов и количество элементов в массиве, и возвращает массив с наибольшей суммой элементов.
def MaxRandomArray(count,num):
    #mat=np.zeros((count,num))
    s=np.zeros(count)
    mat = np.random.uniform(100, size=(count,num))
    for i in range(count):
        s[i]=np.sum(mat[i,:])
    print("Все массивы")
    print(mat)
    print()
    x=s.argmax()

    print(mat[x,:]," наибольшая сумма массива - ", s[x])

print("Введите количество массивов: ")
mas = input()
print("Введите количество элементов в массиве: ")
col = input()

MaxRandomArray(int(mas), int(col))
