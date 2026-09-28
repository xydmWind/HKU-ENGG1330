Packs=int(input())
Budget=int(input())
Value=Packs*15
print(f"Total: {Value}")
if Value<=Budget:
    print("Enough money")
else:
    print("Not enough money")