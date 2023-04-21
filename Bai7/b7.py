# dictA  = dict()
# dictB = dict()
# #Nhập từ điển
# print('Nhập từ điển A:')
# n = int(input('N = '))
# for i in range(n):
#     key = input('Key = ')
#     val = input('Value = ')
#     dictA.update({key: val})
# print('Nhập từ điển B:')
# m = int(input('M = '))
# for i in range(m):
#     key = input('Key = ')
#     val = input('Value = ')
#     dictB.update({key: val})
#
# for i in dictA.keys():
#     if i in dictB:
#         dictA[i] = max(dictA[i], dictB[i])
#         del dictB[i]
# for i in dictB.keys():
#     dictA.update({i: dictB[i]})
# print(dictA)



dictA  = dict()
dictB = dict()
#Nhập từ điển
print('Nhap tu dien A:')
n = int(input('Nhap N:'))
for i in range(n):
    key = input('Nhap khoa:')
    val = input('Nhap gia tri:')
    dictA.update({key: val})
print('Nhap tu dien B:')
m = int(input('Nhap M:'))
for i in range(m):
    key = input('Nhap khoa:')
    val = input('Nhap gia tri:')
    dictB.update({key: val})

for i in dictA.keys():
    if i in dictB:
        dictA[i] = max(dictA[i], dictB[i])
        del dictB[i]
for i in dictB.keys():
    dictA.update({i: dictB[i]})
print('Ket qua:')
for i in dictA.values():
    print(i)
