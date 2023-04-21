s = input('Nhập s:').split()
max = 0
for i in s:
    if len(i)>max:
        max = len(i)
print('Độ dài lớn nhất:',max)
print('Những từ có độ dài lớn nhất:')
for i in s.split():
    if len(i)==max:
        print(i)
