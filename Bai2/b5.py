def Fibo(n):
    if n<4 : return n
    return Fibo(n-2)+Fibo(n-1)

def isFibo(n):
    d = 0
    for i in range (0, n+1):
        if Fibo(i)==n : d = d+1
    if d==1: return True
    else: return False

n = int(input("n = "))
if isFibo(n)==True: print("Thuộc dãy Fibo")
else: print("Không thuộc dãy Fibo")