s = input('Nhập s: ')
n = int(input('N = '))
#hàm trả về giá trị min của dãy
def min(s):
    m = s[:1]
    for i in s:
        if i<m:
            m = i
    return m
#hàm trả về giá trị max của dãy
def max(s):
    m = s[:1]
    for i in s:
        if i>m:
            m = i
    return m
#hàm thực hiện yêu cầu
def returnString(s, n):
    while n>0:
        # nếu kí tự max ở đầu thì xóa các kí tự min
        if s[:1] == max(s):
            s = s.replace(min(s), '', 1)
            n = n - 1
        # nếu kí tự max không ở đầu thì so sánh 2 kí tự gần nhau và xóa kí tự bé hơn, sau đó break
        else:
            for i in range(0, len(s) - 1):
                if s[i:i + 1] < s[i + 1:i + 2]:
                    s = s.replace(s[i:i + 1], '', 1)
                    n = n - 1
                    break
                elif s[i:i + 1] > s[i + 1:i + 2]:
                    s = s.replace(s[i + 1:i + 2], '', 1)
                    n = n - 1
                    break
    return s
print(returnString(s,n))
