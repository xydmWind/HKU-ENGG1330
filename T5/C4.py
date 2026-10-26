q = int(input())
Inventory = []
Step = 0
CheckpointInventory = {0: Inventory[:]}

for i in range(q):
    Command = input().strip()
    if Command == "undo":
        if Step > 0:
            Step -= 1
        Inventory = CheckpointInventory[Step][:]
    else:
        CommandType, Item = Command.split()
        if CommandType == "add":
            Inventory.append(Item)
            Step += 1
            CheckpointInventory[Step] = Inventory[:]
        elif Item in Inventory:
            Inventory.remove(Item)
            Step += 1
            CheckpointInventory[Step] = Inventory[:]
    print(Inventory)