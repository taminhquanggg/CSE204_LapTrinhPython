# n = int(input('n = '))
# D = dict()
# for i in range (n):
#     D.update({i:input('Cách đọc số '+str(i)+' là:')})
# print(D)

n = int(input('Nhap N:'))
D = dict()
for i in range(n):
    D.update({input('Nhap cach doc tieng anh cua so '+str(i)+':'):i})
for i in sorted(D, key=D.get, reverse=True):
    print('Key:',D[i],'Values:', i)
