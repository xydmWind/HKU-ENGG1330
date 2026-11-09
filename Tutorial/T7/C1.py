def undo_readings(readings: list, k: int) -> list:
    removed = [readings.pop() for _ in range(k)]
    return removed


n = int(input())
readings = []
for i in range(n):
    readings.append(int(input()))
k = int(input())
observer = readings
removed = undo_readings(readings, k)
print(removed)
print(readings)
print(observer)