def checkYear(y):
    return (y%4 == 0 and y%100 != 0) or y%400 == 0
def checkMonth(m):
    if m==2:
        return 29 if checkYear(y) else 28
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    elif m==4 or m==6 or m==9 or m==11:
        return 30
def checkDay(d, m, y):
    d=d+1
    if d>checkMonth(m):
        if m==12:
            d=1
            m=1
            y=y+1
        else:
            d=1
            m=m+1
    print(d,"/",m,"/",y)
d = int(input("ngày: "))
m = int(input("tháng: "))
y = int(input("năm: "))
checkDay(d,m,y)