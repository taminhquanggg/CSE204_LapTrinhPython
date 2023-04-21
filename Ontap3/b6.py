n = int(input('N = '))
l = [int(i) for i in range(1, n+1)]
L = []
while len(l)!=1:
    if len(L) < 3:
        for i in l:
            L.append(i)