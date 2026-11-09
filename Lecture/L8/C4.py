def insert_latest(values: list) -> None:
    if len(values) <= 1:
        return None

    tmp_values = []
    target = values[-1]
    done = False

    for i in range(len(values)-1):
        if values[i] < target:
            tmp_values.append(values[i])
            continue
        elif not done:
            tmp_values.append(target)
            done = True
        tmp_values.append(values[i])

    if not done:
        tmp_values.append(target)

    values[:] = tmp_values
    return None


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
observer = values
result = insert_latest(values)
print(values)
print(observer)
print(result)