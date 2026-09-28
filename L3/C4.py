ScoreNum=int(input())
if ScoreNum==0:
    print(0)
else:
    FormerScore=int(input())
    ImpLength=1
    ImpLengthMax=1
    for i in range(ScoreNum-1):
        Score=int(input())
        if Score>FormerScore:
            ImpLength+=1
            if ImpLength>ImpLengthMax:
                ImpLengthMax=ImpLength
        else:
            ImpLength=1
        FormerScore=Score
    print(ImpLengthMax)