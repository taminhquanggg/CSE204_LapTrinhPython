import struct
try:
    f = open(input('File name: '), 'rb')
    x = f.read()
    if x[:2] == b'BM':
        print('Có là ảnh bitmap!\nKích thước: ',end='')
        print(struct.unpack('i', x[18:22])[0],'x',struct.unpack('i', x[22:26])[0])
    else:
        print('Không là ảnh bitmap!')
finally:
    f.close()
