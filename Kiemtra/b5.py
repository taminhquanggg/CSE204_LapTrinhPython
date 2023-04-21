n = int(input("N = "))
d = 0
for i in range(1, n):
    for j in range(1, n):
        k = n - i - j
        if k > 0 and k>=2:
            s = i + j + k
            if s == n:
                if k - 1 > 1:
                    d = d + k - 1
                else:
                    d = d + 1
print("Co",d,"cach phan tich",n,"thanh tong 4 so nguyen duong")