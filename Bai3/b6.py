def fibo(n, k):
    if 0>n:
        return 0
    if n<k:
        return n
    s=0
    for i in range (k, 0, -1):
        s += fibo(n-i, k)
    return s
n = int(input("n = "))
k = int(input("k = "))
print("fibo("+str(n)+","+str(k)+") =", fibo(n, k))

