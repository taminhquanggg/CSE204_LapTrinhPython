n = int(input('N = '))
d = 0
S = 0
for i in range(1, n+1):
    d = d + i**2
    S = S + n/d
print('F('+str(n)+') =', format(S, '.7f'))
