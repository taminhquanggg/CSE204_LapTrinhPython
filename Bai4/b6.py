s = input()
for i in s:
    if s.count(i)!=0:
        print('Kí tự "'+ i +'" xuất hiên '+ str(s.count(i)) +' lần')
        s = s.replace(i, '')