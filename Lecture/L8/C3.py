def bubble_pass(values: list) -> int:
    count = 0

    for i in range(len(values)-1):
        if values[i] > values[i+1]:
            tmp = values[i]
            values[i] = values[i+1]
            values[i+1] = tmp
            count += 1

    return count


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
observer = values
result = bubble_pass(values)
print(result)
print(values)
print(observer)
