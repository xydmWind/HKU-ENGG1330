Code=str(input())
PreCode=''
isUpper=False
isLower=False
isDigit=False
isInvalid=False
if len(Code)<6 or len(Code)>10:
    isInvalid=True
else:
    for i in range(len(Code)):
        if Code[i].isupper():
            isUpper=True
        elif Code[i].islower():
            isLower=True
        elif Code[i].isdigit():
            isDigit=True
        else:
            isInvalid=True
            break
        if PreCode==Code[i]:
            isInvalid=True
            break
        PreCode=Code[i]
if isUpper and isLower and isDigit and not isInvalid:
    print("VALID")
else:
    print("INVALID")