People=int(input())
Budget=int(input())
if People==4:
    Cost=100
else:
    Cost=People*30
print(Cost)
if Cost<=Budget:
    print("Enough money")
else:
    print("Not enough money")