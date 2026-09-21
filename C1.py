fruits=('apple','orange','pear','banana')
Start=int(input())
Stop=int(input())
if Stop-Start<=1:
    print("Empty")
else:
    print(fruits[Start:Stop])