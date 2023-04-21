'''def listPascal(list):
    list1 = [1]
    for i in range(1, len(list)):
        list1.append((list[i-1]) + (list[i]))
    list1.append(1)
    return list1

n = int(input('n = '))
list = [1]
while n>0:
    print(list)
    list = listPascal(list)
    n = n - 1
'''
def next(L):
    N = [1]
    for i in range (len(L)-1):
        N.append(L[i]+L[i+1])
    return N+ [1]
n = int(input('n = '))
L = [1]
print('{:^50}'.format(str(L)))
for k in range(2, n+1):
    L = next(L)         #tạo ra dòng tiếp theo từ dòng hiện tại
    print('{:^50}'.format(str(L)))