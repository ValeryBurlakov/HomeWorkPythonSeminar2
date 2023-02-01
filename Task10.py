import random
n = abs(int(input("Введите количество монеток: ")))
list = []

count = 0
count2 = 0
for i in range(n):
    list.append(random.randint(0, 1))
print("Наши монетки упали таким образом: ")
print(list)
for i in list:
    if i == 0:
        i = 1
        count = count + 1
    elif i == 1:
        i = 0
        count2 = count2 + 1

if count < count2:
    print(f"для того, чтобы все стали одинаковыми с минимальным количеством действий, \nнужно: {count} действий")
else:
    print(f"для того, чтобы все стали одинаковыми с минимальным количеством действий, \nнужно: {count2} действий")