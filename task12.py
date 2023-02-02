import math
s = abs(int(input("Сумма натуральных чисел: ")))
p = abs(int(input("произведение натуральных чисел: ")))

y = (s - int(math.sqrt(s**2 - 4 *  p)))/2
# x = s - y
x = (s + int(math.sqrt(s**2 - 4 * p)))/2
print(int(y), int(x))

# x + y = s
# x * y = p
# система уравнений
# x = s - y
# (s-y)*y = p 

