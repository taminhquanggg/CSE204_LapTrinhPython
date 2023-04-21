def check(a):
    if a<=0:
        raise ValueError('Bạn phải nhập số lớn hơn 0!')
    return a
try:
    a = float(input('a = '))
    check(a)
    b = float(input('b = '))
    check(b)
    c = float(input('c = '))
    check(c)
except ValueError:
    print('Không phải giá trị số')
else:
    try:
        if a<=0 or b<=0 or c<=0:
            raise ValueError('Giá trị độ dài không đúng')
        if a+b<=c or a+c<=b or b+c<=a:
            raise ValueError('Giá trị nhập vào không thể là 3 cạnh của tam giác')
    except ValueError as ex:
        print(ex)
    else:
        print('Done!')