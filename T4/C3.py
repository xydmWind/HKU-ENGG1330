CommandNum=int(input())
CommandList=[]
isKeyTaken=False
isDoorOpen=False
for i in range(CommandNum):
    CommandList.append(' '.join(str(input()).lower().split()))
for i in range(CommandNum):
    if CommandList[i]=="take key":
        if isKeyTaken:
            print("ALREADY HAVE KEY")
        else:
            isKeyTaken=True
            print("KEY TAKEN")
    elif CommandList[i]=="look":
        if isDoorOpen:
            print("DOOR OPEN")
        else:
            print("DOOR LOCKED")
    elif CommandList[i]=="open door":
        if isDoorOpen:
            print("ALREADY OPEN")
        elif isKeyTaken:
            isDoorOpen=True
            print("DOOR OPENED")
        else:
            print("LOCKED")
    else:
        print("UNKNOWN")