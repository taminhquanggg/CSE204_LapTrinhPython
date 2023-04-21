n = int(input("N = "))
d = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            for l in range(1, n+1):
                if i%2 == 0 and j%2 == 0 and k%2 == 0 and l%2 == 0:
                    s = i + j + k + l
                    if s == n:
                        d = d + 1
print("Co",d,"cach phan tich",n,"thanh tong 4 so nguyen duong")