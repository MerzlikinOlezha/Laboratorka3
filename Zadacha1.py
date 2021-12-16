import random
minus = []
plus = []
def view(mas):
    for x in mas:
        if x <= 0:
            minus.append(x)
        else:
            plus.append(x)
            plus.reverse()
    for i in range(0, len(mas), 10):
        print(*mas[i: i + 10])
mas = [random.randint(-30, 45) for i in range(0, 75)]
view(mas)
print('Числа больше 0:', plus)
