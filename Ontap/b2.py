def Fibo(n):
    return n if n<2 else Fibo(n-1)+Fibo(n-2)
n = int(input('n = '))
i = 0
while True:
    if Fibo(i+1)<n:
        i += 1
    else:
        print(Fibo(i))
        break
