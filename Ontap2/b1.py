s = input('Nhập dãy: ').split(',')

def KT(l):
    for i in range(max(l)):
        if i+1 == l[i]:
            continue
        else:
            return False
    return True

print('Có là dãy hoán vị' if KT(sorted([int(i) for i in s])) else 'Không là dãy hoán vị')
