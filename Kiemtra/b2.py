n = int(input("N = "))
l, k = 0, 0
for i in range(1, n+1):
    k = k + i
    l = l + float(i/k)
print("F(" + str(n) + ") =", format(l, '.6f'))