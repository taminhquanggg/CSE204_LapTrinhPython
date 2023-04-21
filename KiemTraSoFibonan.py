n = int(input("Nhập số dương N: "))
a, b = 0, 1
while b!=n:
    if b>n:
        break
    a, b = b, a+b
print("Fibonacci" if b==n else "Non-fibonacci")