def reload(n):
    s, l = 0, len(n)
    for i in n:
        l = l-1
        s = int(s) + int(i)*2**(l)
    return s
s = input('Nhập chuỗi:').split(sep=',')
for w in s:
    #print(reload(w))
    print(int(w, 2),' ')