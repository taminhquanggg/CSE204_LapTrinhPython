def area(a, b, c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

print("Nhập độ dài các cạnh của tam giác:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("Diện tích tam giác là: S = ",area(a, b, c))