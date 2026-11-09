def find_sensor(values: list, target: int) -> int:
    position = -1

    for i in range(len(values)):
        if values[i] == target:
            position = i
            break

    return position


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
target = int(input())
result = find_sensor(values, target)
print(result)
print(values)