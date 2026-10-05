PlainText=str(input())
CipherText=""
Key=int(input())
for i in range(len(PlainText)):
    if PlainText[i]==" ":
        CipherText+=" "
    else:
        CipherText+=chr((ord(PlainText[i])-ord('a')+26-Key)%26+ord('a'))
print(CipherText)