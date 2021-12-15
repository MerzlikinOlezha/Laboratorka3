# 6 Задание Готово(выполнено по заданию)
# sumRecursive – рекурсивно вычисляет сумму элементов массива
def sum_rec(arr, size): # Вводим аргумент в функцию
    if (size == 0): # Условие
        return 0
    else:
        return arr[size - 1] + sum_rec(arr, size - 1)
n = int(input("Введите длину списка:"))
a = []
for i in range(0, n):
    element = int(input("Введите элемент списка:"))
    a.append(element)
print("Весь список:")
print(a)
print("Сумма элементов списка равна:")
b = sum_rec(a, n)
print(b)


# sumIterative – итерационно вычисляет сумму элементов массива
z1 = int(input("\n\nВведите длину списка:"))
z = []
for t in range(0, z1):
    element = int(input("Введите элемент списка:"))
    z.append(element)
print("Весь список:")
print(z)
def sum_itt(z, b): #аргументы
    res = 0
    for i in range(b - 1, len(z)): # len - длина проекта
        res += sum([z[j] for j in range(i, i - b, -1)]) / b
    return res
print("Результат итерационной суммы в данном массиве: " , sum_itt(z, 3))



# minIterative – итерационно вычисляет минимальный элемент в массиве
l1 = int(input("\n\nВведите длину списка:"))
l = []
for t1 in range(0, l1):
    element = int(input("Введите элемент списка:"))
    l.append(element)
print("Весь список:")
print(l)
smallest_number = min(l)
print("Минимальный элемент в данном массиве(Итерационно): ", smallest_number)



# minRecursive – рекурсивно вычисляет минимальный элемент в массиве
def recursiv_minimum(l, val):
  if not l[1:]:
     return val
  return recursiv_minimum(l[1:], l[0] if l[0] < val else val) # Двоетачие говорит откуда мы начинаем
l = [34, 23, 2, 4, 18]
print("\n\nМинимальный элемент в данном массиве(Рекурсией): ", recursiv_minimum(l, l[0]))
print(l)
