
def area2(xa, ya, xb, yb, xc, yc):
    ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
    bc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5
    p = (ab + bc + ac) / 2
    return (p * (p - ab) * (p - bc) * (p - ac)) ** 0.5


xa, ya = map(float, input().split())
xb, yb = map(float, input().split())
xc, yc = map(float, input().split())

print("Diện tích tam giác là:",area2(xa, ya, xb, yb, xc, yc))