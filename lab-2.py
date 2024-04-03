# Исходная матрица A
A = [[2, 3], [-1, 0]]

# Матрица перехода P и ее обратная P_inv
P = [[-1, 1, 0], [1, -2, 0], [0, 0, 1]]
P_inv = [[-2, -1, 0], [-1, -1, 0], [0, 0, 1]]

# Функция для умножения матриц
def matrix_multiply(M1, M2):
    result = []
    for i in range(len(M1)):
        row = []
        for j in range(len(M2[0])):
            summa = 0
            for k in range(len(M2)):
                summa += M1[i][k] * M2[k][j]
            row.append(summa)
        result.append(row)
    return result

# Расширяем матрицу A до 3x3
A_expanded = A + [[0, 0]]
for row in A_expanded:
    row.append(0)

# Вычисляем A' = P_inv * A * P
A_prime = matrix_multiply(matrix_multiply(P_inv, A_expanded), P)

# Выводим результат
for row in A_prime:
    print(row)
