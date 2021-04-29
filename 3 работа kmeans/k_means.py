import numpy as np


# евклидово расстояние между двумя точками
def dist(A, B):
    # TODO: реализуйте вычисление евклидова расстояния для двух точек A и B в N-мерном пространстве
    # Помните, что размерность пространства может быть произвольной (не только 2D).

    # Для взятия разностей по каждому измерерию можно использовать код: A - B

    # Для возведения в квадрат можете использовать оператор ** (например, 3**2 == 9) или функцию np.power
    # Для вычисления суммы используйте функцию sum или np.sum
    # Для вычисления квадратного корня используйте функцию np.sqrt
    # r = ...
    # ВЫЧИСЛЯЕМ РАЗНОСТЬ КООРДИНАТ
    V = A - B
    # ВОЗВОДИМ ИХ В КВАДРАТ
    V2 = np.power(V, 2)
    # НАХОДИМ КОРЕНЬ ИЗ СУММЫ КВАДРАТОВ
    r = np.sqrt(np.sum(V2))

    return r


# возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):
    m = len(X)
    k = len(centers)

    # матрица расстояний от каждой точки до каждого центра
    distances = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            distances[i, j] = dist(centers[j], X[i])

    # поиск ближайшего центра для каждой точки
    return np.argmin(distances, axis=1)


def kmeans(k, X):
    # TODO: инициализировать переменные m и n
    # m - количество строк в матрице X
    # n - количество столбцов в матрице X
    # Используйте свойство shape матрицы X для решения этой задачи
    # Чтобы понять, что хранится в свойстве shape, попробуйте в консоли Python следующий код:
    # >>> ones = np.ones((3, 2))
    # >>> ones
    # >>> ones.shape
    # m = ...  # количество строк в матрице X
    # n = ...  # количество столбцов в матрице X
    # ПОЛУЧАЕМ РАЗМЕРНОСТЬ МАТРИЦЫ
    m, n = X.shape

    curr_iteration = prev_iteration = np.zeros(m)

    # TODO: сгенерировать k кластерных центров со случайными координатами.
    # Должна получиться матрица случайных чисел размера k*n (k строк, n столбцов).
    # Для генерации матрицы случайных чисел используйте код:
    #   centers = np.random.random((k, n))
    # Функция random генерирует случайные числа в диапазоне от 0 до 1, поэтому
    # не забывайте, что координаты центров не должны выходить
    # за границы минимальных и максимальных значений столбцов (признаков) матрицы X.
    # Для вычисления минимальных и максимальных значений по столбцам (признакам)
    # матрицы X используйте функции min(X, axis=0) и max(X, axis=0) библиотеки NumPy соответственно.
    # centers = ...
    # ПОЛУЧАЕМ РАНДОМНЫЕ координаты в диапазоне от 0 до 1
    centers = np.random.random((k, n))
    # ПРИВОДИМ ИХ К диапазону значений в столбцах
    centers = centers * (np.max(X, axis=0) - np.min(X, axis=0)) + np.min(X, axis=0)

    # приписываем каждую точку к заданному классу
    curr_iteration = class_of_each_point(X, centers)

    # цикл до тех пор, пока центры не стабилизируются
    # TODO: условие выхода из цикла - векторы curr_iteration и prev_iteration стали равны
    # Для сравнения двух массивов NumPy можете использовать один из вариантов:
    #   np.all(a1 == a2), где a1 и a2 массивы NumPy.
    # или
    #   np.any(a1 != a2)
    # Для реализации логического отрицания в Python используйте not
    # Поэкспериментируйте в консоли Python с функциями all и any, чтобы понять, как они работают.
    while True:

        prev_iteration = curr_iteration

        # вычисляем новые центры масс
        for i in range(k):
            sub_X = X[curr_iteration == i, :]
            if len(sub_X) > 0:
                centers[i, :] = np.mean(sub_X, axis=0)

        # приписываем каждую точку к заданному классу
        curr_iteration = class_of_each_point(X, centers)
        # ЕСЛИ С ПРЕДЫДУЩЕЙ ИТЕРАЦИИ ЗНАЧЕНИЯ НЕ ИЗМЕНИЛИСЬ, ЦИКЛ ЗАКОНЧЕН
        if np.all(prev_iteration == curr_iteration):
            break

    return centers
