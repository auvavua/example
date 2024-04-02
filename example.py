import numpy as np
import time

# Создание двух матриц размером 1500x1500
matrix1 = np.random.rand(150, 150)
matrix2 = np.random.rand(150, 150)

# Функция для умножения матриц
def multiply_matrices(matrix1, matrix2):
    result = np.zeros((len(matrix1), len(matrix2[0])))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Измерение времени выполнения для варианта 1: i, j, k
start_time = time.time()
result1 = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Время выполнения (вариант 1):", end_time - start_time, "секунд")

# Измерение времени выполнения для варианта 2: i, k, j
start_time = time.time()
result2 = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Время выполнения (вариант 2):", end_time - start_time, "секунд")

# Измерение времени выполнения для варианта 3: j, i, k
start_time = time.time()
result3 = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Время выполнения (вариант 3):", end_time - start_time, "секунд")

# Измерение времени выполнения для варианта 4: j, k, i
start_time = time.time()
result4 = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Время выполнения (вариант 4):", end_time - start_time, "секунд")

# Измерение времени выполнения для варианта 5: k, i, j
start_time = time.time()
result5 = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Время выполнения (вариант 5):", end_time - start_time, "секунд")

# Измерение времени выполнения для варианта 6: k, j, i
start_time = time.time()
result6 = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Время выполнения (вариант 6):", end_time - start_time, "секунд")
