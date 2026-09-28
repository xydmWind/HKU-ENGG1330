Rooms=int(input())
Coins=int(input())
if Rooms%12==0:
    PacksNum=Rooms//12
else:
    PacksNum=Rooms//12+1
print(str(PacksNum)+"\n"+str(PacksNum*7)+"\n"+str(bool((PacksNum*7)<=Coins)))