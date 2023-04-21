S = set()
while True:
    s = input('Nhập họ tên:')
    if s.title()!=s:
        break
    S.add(s)
print(S)