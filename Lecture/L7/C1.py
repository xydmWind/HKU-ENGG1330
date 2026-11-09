def adjust_in_place(readings: list, offset: int) -> None:
    for i in range(len(readings)):
        readings[i] += offset
    return None


n = int(input())
readings = []
for i in range(n):
    readings.append(int(input()))
offset = int(input())
observer = readings
result = adjust_in_place(readings, offset)
print(readings)
print(observer)
print(result)
