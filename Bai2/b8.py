def max(a, b):
    return a if a>=b else b

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("MAX =", max(max(a,b),c))
if a==b and max(a,b)==a:
    print(c)
elif a==c and max(a,c)==a:
    print(b)
elif b==c and max(b,c)==c:
    print(a)

