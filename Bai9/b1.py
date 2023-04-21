try:
    with open('b1.txt', encoding='utf-8') as f:
        s = f.readlines(2)
        print(s)
finally:
    f.close()