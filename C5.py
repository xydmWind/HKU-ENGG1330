VisitorsNum=int(input())
if VisitorsNum==0:
    print(str(0)+"\n"+str(0))
else:
    VisitorsName=[]
    for i in range(VisitorsNum):
        VisitorsName.append(str(input()))
    RunLengthMax=0
    RunStart=1
    for Start in range(VisitorsNum):
        Run=set()
        for i in range(Start,VisitorsNum):
            if VisitorsName[i] in Run:
                break
            Run.add(VisitorsName[i])
        RunLength=len(Run)
        if RunLength>RunLengthMax:
            RunLengthMax=RunLength
            RunStart=Start+1
    print(str(RunStart)+"\n"+str(RunLengthMax))