# 360 độ
# 60 phút kim phút quay 360 độ
# -> 1 phút kim phút quay 6 độ
# 12 giờ kim giờ quay 360 độ
# -> 60 phút kim giờ quay 30 độ
# -> 1 phút kim giờ quay 0.5 độ
# => kết quả = abs(kim phút - kim giờ)
# abs( số phút * 6 độ - 0.5 độ * (số giờ*60+số phút))

t = [int(i) for i in input('T = ').split(':')]
k = round(abs(t[1]*6 - 0.5*(t[0]*60 + t[1])), 2)
print('Góc:', k if k <= 360 else k-360,'độ')
