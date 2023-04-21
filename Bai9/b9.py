try:
    f1 = open(input('File 1:'), encoding='utf-8')
    f2 = open(input('File 2:'), encoding='utf-8')
    s1, s2 = f1.read(), f2.read()
    print('Giống' if s1==s2 else 'Khác')
finally:
    f1.close()
    f2.close()