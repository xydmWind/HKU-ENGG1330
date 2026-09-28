Energy=int(input())
Has_Key=int(input())
Knows_Code=int(input())
if Energy>=5 and (Has_Key or Knows_Code):
    print("True")
else:
    print("False")