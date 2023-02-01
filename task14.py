n = int(input("до какого числа?: "))
num = 0
two = 2
res = 0
while res < n:
    res = two**num
    num = num + 1
    if res < n:
        print(res)

