#B9
def checkYear(y):
    return True if (y%100 != 0 and y%4 == 0) or y%400==0 else False
def checkMonth(m, y):
    if m == 2 and checkYear(y):
        return 29
    elif m == 2 and checkYear(y)==False:
        return 28
    elif m in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
def checkDay(d, m, y):
    if d < checkMonth(m, y):
        d = d + 1
    else:
        d = 1
        if m < 12:
            m = m + 1
        else:
            m = 1
            y = y + 1
    print(d, '/', m, '/', y)

d = int(input('d = '))
m = int(input('m = '))
y = int(input('y = '))
checkDay(d, m, y)



