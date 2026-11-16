def find_component(values, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return find_component(values, target, mid + 1, high)
    else:
        return find_component(values, target, low, mid - 1)


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
target = int(input())
print(find_component(values, target, 0, len(values) - 1))
print(values)