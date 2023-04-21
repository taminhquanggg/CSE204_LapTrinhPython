numOfPlayer = int(input('Nhập số người chơi: '))
listPlayer = []
for i in range(numOfPlayer):
    listPlayer.append(set(input('Nhập bộ 6 số của người '+ str(i)+':').split()))
numOfWinner = set(input('Nhập giải đặc biệt:').split())

#Điều kiện thắng giải:
for w in range(numOfPlayer):
    if len(numOfWinner-listPlayer[w])==1:
        print('Người chơi',w,':',listPlayer[w],'thắng giải nhất')
    elif len(numOfWinner-listPlayer[w])==0:
        print('Người chơi',w,':',listPlayer[w],'thắng giải đặc biệt')