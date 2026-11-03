def record_reading(readings, value: int) -> bool:
    if 0 <= value <= 100:
        readings.append(value)
        return True
    else:
        return False


n = int(input())
readings = []
for _ in range(n):
    readings.append(int(input()))
value = int(input())
accepted = record_reading(readings, value)
print(accepted)
print(readings)