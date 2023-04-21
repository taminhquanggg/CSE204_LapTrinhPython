prices = dict()
stock = dict()
print('Nhập giá theo loại trái cây!')
while True:
    key = input('Nhập loại trái cây:')
    if key == '':
        break
    value = float(input('Nhập giá:'))
    prices.update({key: value})
print('Nhập số lượng hàng tồn!')
while True:
    key = input('Nhập loại trái cây:')
    if key == '':
        break
    value = int(input('Nhập số hàng tồn:'))
    stock.update({key: value})
#Tạo từ điển lưu kết quả
D = dict()
for i in prices.keys():
    if i in stock:
        D.update({i: prices[i]*stock[i]})
    else:
        D.update({i: prices[i] * 0})
#Tạo list sắp xếp giá trị
List = [i for i in D.values()]
List.sort()
#In ra giá trị
for i in List[::-1]:
    for j in D:
        if i == D.get(j):
            print(j, '\t', int(i))
