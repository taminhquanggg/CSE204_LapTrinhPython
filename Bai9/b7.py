try:
    with open('abc.txt', encoding='utf-8') as f1:
        with open('xyz.txt','w') as f2:
            for i in f1:
                f2.write(i.upper())
finally:
    f1.close()
    f2.close()