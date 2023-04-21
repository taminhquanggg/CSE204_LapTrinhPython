def isPrime(n):
    t = 2
    if n<2: return False
    while t<n:
        if n%t==0:
            return False
        t +=1
    else:
        return True
def snt(n):
    L = []
    for k in range(2, n):
        if isPrime(k):
            L.append(k)
    return L
t = tuple(snt(1000000))
print(t)

