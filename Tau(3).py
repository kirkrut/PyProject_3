import time
import numpy as np

# Ввод матрицы
def input_matr():
    n = int(input())
    print()
    a = []
    for i in range(n):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)

    return a

# Нахождение минора iой строки и jтого столбца
def minor_matr(A, i, j):
    minor = [row for k, row in enumerate(A) if k != i]
    minor = [col for k, col in enumerate(zip(*minor)) if k != j]
    return minor


# Вычисление определителя
def det_matr(A):
    if len(A) == 1:
        return A
    elif len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        return sum((-1) ** j * A[0][j] * det_matr(minor_matr(A, 0, j))
                   for j in range(len(A[0])))


# Вычисление ранга матрицы
def rang_matr(A):
    if len(A) < len(A[0]):
        c = len(A)
    else:
        c = len(A[0])
    count = 1
    rang = 0
    while count <= c:
        R = [[]] * count
        for i in range(count):
            R[i] = [1] * count
        for j in range(len(A) - count + 1):
            for l in range(len(A[0]) - count + 1):
                for k in range(count):
                    for f in range(count):
                        R[k][f] = A[j + k][l + f]
                    if det_matr(R) != 0:
                        rang = count
        count += 1

    return rang


def perform():
    print("Введите матрицу")
    matrix = input_matr()
    start = time.time()
    print("Ранг матрицы: " + str(rang_matr(matrix)))
    finish = time.time()
    print("Время вычисления ранга: " + str(finish - start))
    start = time.time()
    print("Ранг матрицы с помощью numpy: " + str(np.linalg.matrix_rank(matrix)))
    finish = time.time()
    print("Время вычисления ранга с помощью numpy: " + str(finish - start))
    if rang_matr(matrix) == len(matrix):
        print("Система управляема и наблюдаема")
    else:
        print("Система не управляема и не наблюдаема")


perform()