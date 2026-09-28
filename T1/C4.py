Cost=int(input())*30
Budget=int(input())
if Cost<=Budget:
    print("Remaining:",Budget-Cost)
else:
    print("Need:",Cost-Budget)