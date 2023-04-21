try:
    with open('abc.txt', encoding='utf-8') as f1:
        s = f1.read()
        with open('number.txt', 'w', encoding='utf-8') as f2:
            for i in s:
                if i.isdigit():
                    f2.writelines(i+'\n')
finally:
    f1.close()
    f2.close()