s = input('s = ')
print('Có' if s.endswith('!!!') else s + '!'*(3- s.count('!', len(s) - 3, len(s))))