def giaithua(n):
    gt = n;
    if n == 0 :
        return 1;
    gt = gt*giaithua(n-1)
    return gt

n = int(input("n = "))
print(str(n) + "! = ", giaithua(n))
