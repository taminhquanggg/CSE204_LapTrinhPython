a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
delta = b**2 - 4*a*c

if delta > 0:
    print("Phuog trinh co hai nghiem phan biet:\n")
    print("x1 = " + str((-b - delta ** 0.5) / (2*a)))
    print("x2 = "+ str((-b + delta ** 0.5) / (2*a)))

elif delta<0:
    print("Phuong trinh vo nghiem")

else:
    print("Phuong trinh co nghiem kep:\n")
    print("x1 = x2 = " + str(-b/(2*a)))
