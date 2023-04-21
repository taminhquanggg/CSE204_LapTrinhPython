dictValue = dict()
listOfMaxValue = []
#Nhập lượng mưa
for i in range(12):
    List = []
    print('Nhập lượng mưa của tháng', i+1, 'từ năm 2000 đến 2019 (cách nhau bởi dấu phẩy):')
    s = input().split(',')
    # Thêm số liệu lượng mưa vào từ điển
    dictValue.update({i + 1: s})
    #Thêm số liệu lượng mưa vào list
    for i in range(len(s)):
        List.append(int(s[i]))
    #Thêm số liệu lượng mưa lớn nhất vào list
    listOfMaxValue.append(max(List))

month, year = 0, 0
#Tìm ra lượng mưa lớn nhất
maxValue = max(listOfMaxValue)
#Tìm tháng có lượng mưa lớn nhất
for i in range(len(listOfMaxValue)):
    if listOfMaxValue[i] == maxValue:
        month = i
        break

#Tìm năm có lượng mưa lớn nhất
listOfMaxMonth = []
for i in dictValue.keys():
    listOfMaxMonth = dictValue[month+1]
for i in range(len(listOfMaxMonth)):
    if int(listOfMaxMonth[i]) == maxValue:
        year = i
        break

#In ra lượng mưa lớn nhất kèm năm/ tháng đầu tiên
if year<10:
    print('Lượng mưa lớn nhất :', maxValue, 'vào tháng', month+1, 'năm 200'+ str(year))
else:
    print('Lượng mưa lớn nhất :', maxValue, 'vào tháng', month+1, 'năm 20'+ str(year))