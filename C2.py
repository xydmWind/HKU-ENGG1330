Visitors=set()
while True:
    Name=str(input())
    if Name=="END":
        print("None")
        break
    else:
        if Name in Visitors:
            print(Name)
            break
    Visitors.add(Name)