NumN=int(input())
ItemsN=set()
for i in range(NumN):
    ItemsN.add(str(input()))
NumM=int(input())
ItemsM=set()
for i in range(NumM):
    ItemsM.add(str(input()))
Items=['compass','key','map','torch']
SharedItemExists=bool(False)
for i in Items:
    if i in ItemsN and i in ItemsM:
        print(i)
        SharedItemExists=True
if not SharedItemExists:
    print("NONE")