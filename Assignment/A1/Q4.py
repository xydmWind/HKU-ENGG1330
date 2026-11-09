RowNum=int(input())
ColumnNum=int(input())
Size=int(input())
Tile=""
for Row in range(RowNum):
    if Row%2==0:
        Tile="#"
    else:
        Tile="."
    RowOutput=""
    for Column in range(ColumnNum):
        for SColumn in range(Size):
            RowOutput+=Tile
        if Tile=="#":
            Tile="."
        else:
            Tile="#"
    for SRow in range(Size):
        print(RowOutput)