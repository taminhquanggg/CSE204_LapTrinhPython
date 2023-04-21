Dict = dict()
try:
    with open('b5.txt', encoding='utf-8') as f:
        s = f.read()
        for i in s:
            if i.isalpha():
                Dict.update({i: s.count(i)})
    print(Dict)
finally:
    f.close()