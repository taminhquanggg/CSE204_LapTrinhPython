a = 10000000

for i in range (1, 11):
    a = a + a*0.051
print("Số tiền sau 10 năm là: "+str(a)+" VNĐ")

a = 10000000
d=0

while (a<50000000):
    a = a + a * 0.051
    d = d + 1

print("Sau "+str(d)+" năm sẽ có ít nhất 50 triệu đồng")