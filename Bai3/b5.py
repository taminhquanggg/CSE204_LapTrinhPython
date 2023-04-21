def UCLN(a,b):
    while (a>0 and b>0):
        if (a>b):
            a%=b
        else:
            b%=a
    return a+b
def BCNN(a, b):
    return (a*b)/UCLN(a,b)
bcnn = 1
ucln = 0
while True:
    n = int(input("n = "))
    if n <= 0:
        break
    ucln, bcnn = UCLN(n, ucln), BCNN(n, bcnn)
print("UCLN = ",ucln)
print("BCNN = ", int(bcnn))