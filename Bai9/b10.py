import os
def Output(l):
    s, D = set(), dict()
    for i in range(len(l)):
        f = open(l[i], encoding='utf-8')
        s.update(f.read())
        f.close()
    for j in s:
        k = []
        for i in range(len(l)):
            f = open(l[i], encoding='utf-8')
            if f.read() == j:
                k.append(l[i])
            f.close()
        D.update({tuple(k): len(k)})
    for i in sorted(D, key=D.get, reverse=True):
        print(i,'\t', D[i])

l = [x[2] for x in os.walk(r'C:\Users\admin\Desktop\Python\Bai9')]
listFile = []
for i in l[0]:
    if i.endswith('.txt'):
        listFile.append(i)
Output(listFile)