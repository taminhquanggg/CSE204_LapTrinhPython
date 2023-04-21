# -1,4,5,3,6,3,8
s = input('Nhập dãy: ').split(',')
l1 = sorted([int(i) for i in s if int(i) % 2 == 0], reverse=True)
for i in sorted([int(i) for i in s if int(i) % 2 != 0]):
    l1.append(i)
print(l1)