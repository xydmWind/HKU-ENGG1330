def find_component(values: list, target: int) -> int:
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
target = int(input())
result = find_component(values, target)
print(result)
print(values)
