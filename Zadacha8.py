# 8 Задание Готово(выполнено по заданию)
def determinant(matrix, mul):
    br = len(matrix)
    if br == 1:
        return mul * matrix[0][0]
    else:
        s = -1
        a = 0
        for i in range(br):
            m = []
            for j in range(1, br):
                buff = []
                for k in range(br):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            s *= -1
            a = a + mul * determinant(m, s * matrix[0][i])
    return a

print("Введите количество строк и столбцов в первом двумерном массиве(Через пробел): ")
n1, m1 = [int(i) for i in input().split()]
print("Записать элементы первого двумерного массива(Через пробел): ")
test_matrix = [[int(j) for j in input().split()] for i in range(n1)]
max_el1 = test_matrix[0][0]
print(determinant(test_matrix, 1))