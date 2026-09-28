text=input().lower()
Vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in range(len(text)):
    if text[i] in Vowels:
        Vowels[text[i]]+=1
for key in Vowels:
    print(f'{key} {Vowels[key]}')