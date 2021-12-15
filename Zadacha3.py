# 3 Задание Готово(выполнено по заданию)
kol_elementov = int(input("Введите количество элементов массива: "))
elementu = list(map(int, input("Перечислите те самые элементы массива: ").split()))
sdvig = int(input("На сколько элементов надо сдвинуть массив влево: "))
sdvinylos = elementu[-sdvig:] + elementu[:-sdvig]
print("Результат: " + str(sdvinylos))