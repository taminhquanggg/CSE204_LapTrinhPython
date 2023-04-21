def giai_thua(n):
    s=n
    if n==0 : return 1
    s=s*giai_thua(n-1)
    return s

def F(n):
    f=0
    for i in range (1, n+1):
       f=f+giai_thua(i)
    return f

n = int(input("N = "))
print("F(N) =",F(n))
