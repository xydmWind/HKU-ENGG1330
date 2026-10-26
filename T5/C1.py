n = int(input())
rooms = []
for i in range(n):
    rooms.append([int(input()), int(input())])

checkpoint = [room[:] for room in rooms]

q = int(input())
for i in range(q):
    r = int(input())
    c = int(input())
    v = int(input())
    rooms[r][c] = v

print(checkpoint)
print(rooms)
