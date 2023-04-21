n = float(input("Nhập điểm trung bình: "))
if n<3.5:
    print("Xếp loại yếu")
elif n>=3.5 and n<5:
    print("Xếp loại kém")
elif n>=5 and n<6.5:
    print("Xếp loại trung bình")
elif n>=6.5 and n<8:
    print("Xếp loại khá")
elif n>=8 and n<9:
    print("Xếp loại giỏi")
else: print("Xếp loại xuất sắc")