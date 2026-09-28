rooms=['Hall','lab','store','garden']
a=int(input())
b=int(input())
rooms_tmp=rooms[a]
rooms[a]=rooms[b]
rooms[b]=rooms_tmp
for i in rooms:
    print(i)
