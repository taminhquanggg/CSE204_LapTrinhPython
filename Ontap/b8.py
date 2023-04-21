s = input('S = ')
S = {s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)}
print(sorted(S))