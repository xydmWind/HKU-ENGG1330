n=int(input())
inventory=[]
for i in range(n):
    inventory.append(input())
loaded=[]
for i in inventory[:]:
    if i!="coin":
        loaded.append(i)
with open("inventory.txt","w") as file:
    for i in loaded:
        file.write(i+"\n")
print(inventory)
print(loaded)