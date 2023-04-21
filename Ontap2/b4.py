# try:
#     with open('abc.txt', encoding='utf-8') as f1:
#         s = f1.readlines()
#         with open('number.txt', 'w', encoding='utf-8') as f2:
#             for i in s:
#                 if i.isdigit():
#                     f2.writelines(i+'\n')
# finally:
#     f1.close()
#     f2.close()
import math
with open('abc.txt', encoding='utf-8') as f1:
    s = f1.readlines()
    S = []
    with open('xyz.txt', 'w', encoding='utf-8') as f2:
        for i in s:
            if i.count(' ') == 0 or len(i) <= 80:
                S.append(i)
            else:
                k = 0
                l = 1
                while math.ceil(len(i)/80)>=l:
                    m = i[k:80*l]
                    k = m.rfind(' ')
                    if i[k] == ' ':
                        k = k + 1
                    s.append(m[:k])
                    l += 1
        for i in S:
            f2.write(i+'\n')
print(S)


