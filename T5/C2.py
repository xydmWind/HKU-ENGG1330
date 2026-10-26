def Craft(InItems, ReItems):
    LeItems = [InItem[:] for InItem in InItems]
    for Item in ReItems:
        if Item in LeItems:
            LeItems.remove(Item)
        else:
            return "MISSING", InItems 
    return "CRAFTED", LeItems
        

n = int(input())
InItems = []
for i in range(n):
    InItems.append(input())

m = int(input())
ReItems = []
for i in range(m):
    ReItems.append(input())

Ans, InItems = Craft(InItems, ReItems)

print(f"{Ans}\n{InItems}")