Time=int(input())
Type=str(input())
Helmet=str(input())
Charge=0
if Type=='standard':
    Charge=20
    if Time>60:
        Charge+=(Time-31)//30*8
    if Charge>=60:
        Charge=60
else:
    Charge=30
    if Time>60:
        Charge+=(Time-31)//30*12
    if Charge>=100:
        Charge=100
if Helmet=='yes':
    Charge+=5
print("Charge: "+str(Charge))