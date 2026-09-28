rooms={1:'hall',3:'lab',5:'garden'}
Num=int(input())
for i in range(Num):
    Room=int(input())
    if Room in rooms:
        print(rooms[Room])
    else:
        print('UNKNOWN')