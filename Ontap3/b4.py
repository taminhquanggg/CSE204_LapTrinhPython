n = int(input('N = '))
h = int(input('H = '))
for i in range(1, h+1):
    if i % 2 == 0:
        n = 2 * n
    else:
        n = n + int(n * 30 / 100)
print(n)