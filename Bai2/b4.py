def total(n):
    d = 0
    r = 0
    while n>=10:
        r = n % 10
        n = int(n / 10)
        d = d + r
    return d+n

n = int(input("n = "))
print("Tổng các chữ số của", n, "là: ", total(n))