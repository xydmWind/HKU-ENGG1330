def corrected_copy(readings: list, offset: int) -> list:
    tmp_readings = readings[:]
    for i in range(len(tmp_readings)):
        tmp_readings[i] += offset
    return tmp_readings


n = int(input())
readings = []
for i in range(n):
    readings.append(int(input()))
offset = int(input())
corrected = corrected_copy(readings, offset)
print(readings)
print(corrected)
print(corrected is readings)
