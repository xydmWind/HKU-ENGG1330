def remove_matches(items,target):
    for i in items[:]:
        if i==target:
            items.remove(i)
n=int(input())
items=[]
for i in range(n):
    items.append(int(input()))
target=int(input())
saved=items[:]
view=items
remove_matches(items,target)
print(view)
print(saved)