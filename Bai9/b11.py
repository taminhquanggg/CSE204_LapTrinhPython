try:
    f = open(input('File name: '), 'rb')
    x = f.read()
    print('Có là tập ảnh jpg !' if x[6:10] == b'JFIF' else 'Không là tập ảnh jpg !')
finally:
    f.close()