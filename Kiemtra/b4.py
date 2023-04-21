n = int(input("Nhap S: "))
A, B, C = [], [], []
for i in range(n):
    k = input("Nhap gia tri thu " + str(i + 1) + ": ")
    try:
        d = int(k)
        A.append(int(k))
    except ValueError:
        B.append(k)
i = 0
while i <len(B):
    k = B[i]
    try:
        d = float(B[i])
    except ValueError:
        B.pop(i)
        C.append(k)
    else:
        i = i + 1
b = [float(i) for i in B]
print("A =",A)
print("B =",b)
print("C =",C)