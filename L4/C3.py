text=input()
CleanText=''
for i in range(len(text)):
    if text[i].isalnum():
        CleanText+=text[i].lower()
if CleanText==CleanText[::-1]:
    print('YES')
else:
    print('NO')