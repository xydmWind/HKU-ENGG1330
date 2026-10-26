Threshold = int(input())
Rooms = {}

with open("visits.txt", "r") as File:
    for Line in File:
        Line = Line.strip()
        if not Line:
            continue
        Room, Score = Line.split()
        if Room not in Rooms or int(Score) > int(Rooms[Room]):
            Rooms[Room] = Score

QualifiedRooms = []
for Room in sorted(Rooms):
    if int(Rooms[Room]) >= Threshold:
        QualifiedRooms.append((Room, Rooms[Room]))

with open("report.txt", "w") as File:
    for Room, Score in QualifiedRooms:
        File.write(f"{Room} {Score}\n")

print(len(Rooms))
print(len(QualifiedRooms))