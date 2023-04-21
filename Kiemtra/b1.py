L = []
L.append(int(input("A = ")))
L.append(int(input("B = ")))
L.append(int(input("C = ")))
L.sort()
k = L[1] - L[0]
print("Nhiem vu hoan thanh" if L[2] - L[1] == k else "Nhiem vu that bai")