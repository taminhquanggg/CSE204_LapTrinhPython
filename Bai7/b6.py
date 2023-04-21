L = []
D = dict()
#Nhập lượng mưa năm 2000 trước để tạo list
print('NĂM 2000')
for j in range(12):
    k = int(input('Lượng mưa tháng '+str(j+1)+' : '))
    L.append([k])
#Nhập lượng mưa các năm còn lại theo yêu cầu
for i in range (1,20):
    print('NĂM 200' + str(i) if i < 10 else 'NĂM 20' + str(i))
    for j in range(12):
        k = int(input('Lượng mưa tháng ' + str(j + 1) + ' : '))
        L[j].append(k)
#Lượng mưa lớn nhất
k = max(max(L))
#Từ điển lưu lượng mưa
for i in range(12):
    D.update({i+1:L[i]})
#In ra từ điển
print('Lượng mưa: ')
for i in D.items():
    print(i)
#Tìm tháng có lượng mưa lớn nhất
month = 0
for i in D.keys():
    if max(D[i])==k:
        month = i
        break
#List tháng xuất hiện lượng mưa lớn nhất
monthMax = L[month-1:month]
listMonthMax = monthMax[0]
#Tìm năm của tháng có lượng mưa lớn nhất
year = 0
for i in range (20):
    if listMonthMax[i]==k:
        year = i
        break
#In ra thông tin tháng/năm có lượng mưa lớn nhất
if year<10:
    print('Tháng ' + str(month) + ' năm 200' + str(year) + ' có lượng mưa lớn nhất: ' + str(k))
else:
    print('Tháng ' + str(month) + ' năm 20' + str(year) + ' có lượng mưa lớn nhất: ' + str(k))
