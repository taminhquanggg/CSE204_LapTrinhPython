n = int(input('n = '))
def doiXung(n):
    return n[::] == n[::-1]
while True:
    if doiXung(str(n)) == True:
        print(n)
        break
    else:
        n = n-1