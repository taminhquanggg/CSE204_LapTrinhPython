d, t, d1 = 0, 0, 0
while True:
    # Nhập dữ liệu
    try:
        n = int(input('n = '))
    # Ngoại trừ khi nhập số khác nguyên
    except ValueError:
        print('Lỗi nhập số')
    else:
        try:
            # Nếu nhập 0 -> break
            if n == 0:
                break
            # Tự sinh ngoại lệ khi nhập số âm
            if n < 0:
                raise ValueError('Lỗi số âm!!!')
            # Tự sinh ngoại lệ nhập lặp
            if t == n:
                d = d + 1
                t = n
            else:
                d = 1
                t = n
            if d == 4:
                d = 0
                d1 = 0
                raise ValueError('Lỗi nhập lặp')
            # Tự sinh ngoại lệ nhập chẵn
            if n % 2 == 0:
                d1 = d1 + 1
            else:
                d1 = 0
            if d1 == 5:
                d = 0
                d1 = 0
                raise ValueError('Lỗi nhập chẵn')
        except ValueError as ex:
            print(ex)
