try:
    A = [int(i) for i in input('Dãy A: ').split(' ')]
    B = [int(i) for i in input('Dãy B: ').split(' ')]
    m = min([i for i in A if i not in B])
except ValueError:
    print('Không có')
else:
    if A.count(m)>1:
        for i in range(len(A)-1, 0, -1):
            if A[i] == m:
                print(m,' vị trí: ',i)
                break
    else:
        print(m)