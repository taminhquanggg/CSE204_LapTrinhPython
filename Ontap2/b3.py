# 5,4,3,4,5,3,1,8,7
s = input('Nhập dãy: ').split(',')
L = [int(k) for k in s]
listOuput = []
while len(L)>0:
    listResult, i = [L[0]], 0
    while i<len(L):
        if max(listResult) < L[i]:
            listResult.append(L[i])
            L.remove(L[i])
        else:
            i = i + 1
    L.remove(listResult[0])
    for i in listResult:
        listOuput.append(i)
    listOuput.append('|' if len(L)!=0 else '')
for i in listOuput:
    print(i, end=' ')