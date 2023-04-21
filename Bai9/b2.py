try:
    with open('b2.txt', encoding='utf-8') as f:
        s = f.read().split()
    print(s[len(s)-5:] if len(s)>=5 else s)
finally:
    f.close()