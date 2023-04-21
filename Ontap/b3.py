def phanTich(n):
    l, i = [], 2
    while n > 1:
        if n % i == 0:
            n = n / i
            l.append(i)
        else:
            i += 1
    return l
n = int(input('n = '))
l = phanTich(n)
print(n, end=' = ')
for i in range(len(l)-1):
    print(l[i], end=' x ')
print(l[len(l)-1])