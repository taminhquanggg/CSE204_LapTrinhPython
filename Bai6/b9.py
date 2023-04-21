room1 = set(input('Phòng nhân sự:').split(','))
room2 = set(input('Phòng hành chính:').split(','))
room3 = set(input('Phòng truyền thông:').split(','))
def max(a,b):
    if a>b: return a
    else: return b
numMember = room1 | room2 | room3
print('Số nhân viên của cả 3 phòng :',len(numMember))
memOfAllRoom = room1 & room2 & room3
print('Nhân viên thuộc cả 3 phòng :',memOfAllRoom if len(memOfAllRoom)!=0 else 'Không có nhân viên thuộc cả 3 phòng!')
memOf2Room = (room1 & room2 - memOfAllRoom) | (room2 & room3 - memOfAllRoom) | (room3 & room1 - memOfAllRoom)
onlyOneRoom = (numMember - memOfAllRoom - memOf2Room)
print('Nhân viên chỉ thuộc một phòng:',onlyOneRoom if len(onlyOneRoom)!=0 else 'Không có nhân viên thuộc một phòng!')
max1 = len(room1 & room2)
max2 = len(room2 & room3)
max3 = len(room1 & room3)
max = max(max(max1, max2), max3)
if max==max1:
    print('nhân sự & hành chính')
if max==max2:
    print('hành chính & truyền thông')
if max==max3:
    print('nhân sự & truyền thông')
print('Phòng 1:',min(room1))
print('Phòng 2:',min(room2))
print('Phòng 3:',min(room3))
