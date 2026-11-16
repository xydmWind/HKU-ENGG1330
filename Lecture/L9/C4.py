def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def sort_readings(values):
    if len(values) <= 1:
        return values[:]
    mid = len(values) // 2
    left_readings = sort_readings(values[:mid])
    right_readings = sort_readings(values[mid:])
    return merge(left_readings, right_readings)


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
result = sort_readings(values)
print(result)
print(values)