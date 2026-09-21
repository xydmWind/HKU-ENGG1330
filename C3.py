prices={'apple':5,'bun':8,'juice':12}
stock={'apple':5,'bun':3,'juice':2}
RequestNum=int(input())
TotalCost=0
RequestRejected=0
for i in range(RequestNum):
    ProductName=str(input())
    ProductNum=int(input())
    if stock[ProductName]>=ProductNum:
        TotalCost+=prices[ProductName]*ProductNum
        stock[ProductName]-=ProductNum
    else:
        RequestRejected+=1
print(TotalCost)
print(RequestRejected)