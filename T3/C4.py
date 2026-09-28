Votes={'hall':0,'lab':0,'garden':0}
Num=int(input())
for i in range(Num):
    Votes[input()]+=1
MaxVotes=max(Votes.values())
print(MaxVotes)
for i in Votes:
    if Votes[i]==MaxVotes:
        print(i)