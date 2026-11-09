LockerNum=int(input())
RequestNum=int(input())
Locker=[0]*LockerNum
Rejected=0
FailedCollection=0
for i in range(RequestNum):
    Request=str(input()).split()
    if Request[0]=="D":
        if Locker[int(Request[2])-1]==0:
            Locker[int(Request[2])-1]=int(Request[1])
        else:
            isRejected=True
            for j in range(int(Request[2]),LockerNum):
                if Locker[j]==0:
                    Locker[j]=int(Request[1])
                    isRejected=False
                    break
            if isRejected:
                for j in range(int(Request[2])-1):
                    if Locker[j]==0:
                        Locker[j]=int(Request[1])
                        isRejected=False
                        break
            if isRejected:
                Rejected+=1
    else:
        if Locker[int(Request[1])-1]==0:
            FailedCollection+=1
        else:
            Locker[int(Request[1])-1]=0
LockerOutput=""
for i in range(LockerNum):
    LockerOutput+=" "
    LockerOutput+=str(Locker[i])
print("Lockers:"+LockerOutput)
print("Rejected: "+str(Rejected))
print("Failed collections: "+str(FailedCollection))