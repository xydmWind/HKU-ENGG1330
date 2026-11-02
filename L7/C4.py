def remove_below(readings: list, threshold: int) -> int:
    kept_readings = []
    removed = 0
    for reading in readings:
        if reading >= threshold:
            kept_readings.append(reading)
        else:
            removed += 1
    readings[:] = kept_readings
    return removed


n = int(input())
readings = []
for i in range(n):
    readings.append(int(input()))
threshold = int(input())
observer = readings
removed = remove_below(readings, threshold)
print(removed)
print(readings)
print(observer)
