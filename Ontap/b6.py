l = input('Nhập dãy: ')
n = int(input('N = '))
L = [l[i: i + n] for i in range(len(l) - n + 1)]
k = [int(max(i)) - int(min(i)) for i in L]
for i in range(len(k)):
    if k[i] == min(k):
        print(L[i])