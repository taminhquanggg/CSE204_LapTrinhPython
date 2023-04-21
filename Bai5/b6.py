def Fibo(n):
    if n<2 : return n
    return Fibo(n-2)+Fibo(n-1)
n = int(input('n = '))
print([Fibo(i) for i in range(n+1) if Fibo(i)<n])