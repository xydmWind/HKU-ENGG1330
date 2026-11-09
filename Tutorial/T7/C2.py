def ordered_report(readings: list) -> list:
    return sorted(readings)


n = int(input())
readings = []
for i in range(n):
    readings.append(int(input()))
report = ordered_report(readings)
print(readings)
print(report)
print(report is readings)