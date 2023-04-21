def UCLN(a,b):
    while (a>0 and b>0):

        if (a>b):
            a%=b
        else:
            b%=a
    return a+b

def BCNN(a, b):
    return (a*b)/UCLN(a,b)

a = int(input("A = "))
b = int(input("B = "))
print("UCLN = ", UCLN(a,b))
print("BCNN = ", int(BCNN(a,b)))