def sumOfNum(n):
    return sum([k for k in range(2,n) if n%k==0])

n = int(input('Nhập n:'))
for i in range(n):
    if sumOfNum(i)>i:
        print(i)
