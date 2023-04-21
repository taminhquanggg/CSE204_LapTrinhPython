
def isPrime(n):
    t = 2
    if n<2: return False
    while t<n:
        if n%t==0:
            return False
        t+=1
    else: return True

a = int(input("A = "))
b = int(input("B = "))
for i in range (a, b+1):
    if isPrime(i):
        print(i,end=" ")


