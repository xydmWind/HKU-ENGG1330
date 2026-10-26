def within_target(value: int) -> bool:
    return value >= 18 and value <=26


def count_within_target(readings) -> int:
    Num = 0
    for i in readings:
        if within_target(i):
            Num+=1
    return Num

assert within_target(22) is True
assert within_target(30) is False

n = int(input())
readings = []
for _ in range(n):
    readings.append(int(input()))
print(count_within_target(readings))