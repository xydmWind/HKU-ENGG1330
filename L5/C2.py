n=int(input())
scores=[]
for i in range(n):
    scores.append(int(input()))
ordered=[]
for s in scores:
    ordered.append(s)
ordered.sort()
print(scores)
print(ordered)