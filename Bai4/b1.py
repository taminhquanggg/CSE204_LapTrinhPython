s = input("s = ")
print('YES' if s.count('!', len(s)-3, len(s))==3 else s+'!'*(3-s.count('!', len(s)-3, len(s))))