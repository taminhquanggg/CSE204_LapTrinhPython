try:
    with open('b3.txt', encoding='utf-8') as f:
        s = f.readlines()
    print(max(s, key = len))
finally:
    f.close()