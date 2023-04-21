S = input('S = ')
L = set()
for c in S:
    N = set()
    for w in L:
        N.add(w+c)
    L = L | N | {c}
print(sorted(L, key= lambda e: (len(e),e)))