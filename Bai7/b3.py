# n = int(input('n = '))
# D = dict()
# for i in range (n):
#     D.update({i:int(input('Value = '))})
# S = {i for i in D.values()}
# d = 0
# while d<3:
#     print(max(S))
#     S.remove(max(S))
#     d = d+1


n = int(input('Nhap N:'))
D = dict()
for i in range (n):
    D.update({i:int(input('Nhap gia tri cua key la cac so nguyen '+str(i)+':'))})
S = {i for i in D.values()}
d = 0
s = []
while d<3:
    s.append(max(S))
    S.remove(max(S))
    d = d+1
for i in sorted(s):
    print(i)