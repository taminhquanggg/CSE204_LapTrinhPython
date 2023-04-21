try:
    with open('b4.txt', encoding='utf-8') as f:
        s = f.read().split()
    print(max(s, key=len))
finally:
    f.close()