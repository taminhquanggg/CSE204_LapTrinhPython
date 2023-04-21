Dict = dict()
try:
    with open('b6.txt', encoding='utf-8') as f:
        s = f.read().split()
        Dict.update({i: s.count(i) for i in s})
        for i in sorted(Dict, key=Dict.get, reverse=True):
            print(i,'\t',Dict[i])
finally:
    f.close()
