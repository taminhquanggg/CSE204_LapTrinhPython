x = int(input("X = "))
d = 0
r = 1

while x >= 10:
    x = x/10
    d = d+1

print("Số chữ số:", d+1)
print("Chữ số đầu tiên:", int(x))
