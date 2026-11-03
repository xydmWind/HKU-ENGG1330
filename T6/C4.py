def shift_readings(readings, offset: int):
    tmp_readings = readings[:]
    for i in range(len(readings)):
        tmp_readings[i] = tmp_readings[i] + offset
    return tmp_readings


def count_at_least(readings, minimum: int) -> int:
    count = 0
    for reading in readings:
        if reading >= minimum:
            count += 1
    return count


def calibration_report(readings, offset: int, minimum: int):
    new_readings = shift_readings(readings, offset)
    return new_readings, count_at_least(new_readings, minimum)


# Successful checks produce no output.
assert shift_readings([2, 4], 1) == [3, 5]
assert count_at_least([1, 3, 3], 3) == 2
assert calibration_report([1, 2], 1, 3) == ([2, 3], 1)

n = int(input())
offset = int(input())
minimum = int(input())
readings = []
for _ in range(n):
    readings.append(int(input()))
corrected, passed = calibration_report(readings, offset, minimum)
print(readings)
print(corrected)
print(passed)