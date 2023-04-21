s = input('Nhập dãy: ').split(',')
l1 = [int(i) for i in s]
l2 = [i**2 for i in l1]
print('Chênh lệch =',sum(l1)**2-sum(l2))