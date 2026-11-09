def select_next(values: list, start: int) -> None:
    min_value = start

    for i in range(start, len(values)):
        if values[i] < values[min_value]:
            min_value = i

    if min_value != start:
        values[start], values[min_value] = values[min_value], values[start]

    return None


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
start = int(input())
observer = values
result = select_next(values, start)
print(values)
print(observer)
print(result)