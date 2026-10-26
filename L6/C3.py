def first_over_limit(readings, limit: int):
    for i in readings:
        if i > limit:
            return i

n = int(input())
limit = int(input())
readings = []
for _ in range(n):
    readings.append(int(input()))
print(first_over_limit(readings, limit))