# n = int(input('n = '))
# D = dict()
# for i in range (n):
#     D.update({i:input('Value = ')})
# print({i for i in D.values()})

n = int(input('Nhap N:'))
D = dict()
for i in range(n):
    D.update({i: input('Nhap gia tri cua key '+str(i)+':')})
s = sorted({i for i in D.values()})
for i in s:
    print(i)