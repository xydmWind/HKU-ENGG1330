def find_part(parts: list, target: int) -> int:
    low = 0
    high = len(parts) - 1
    while low <= high:
        mid = (low + high) // 2
        if parts[mid][0] == target:
            return mid
        elif parts[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


n = int(input())
parts = []
for i in range(n):
    code, stock = map(int, input().split())
    parts.append((code, stock))
target = int(input())
print(find_part(parts, target))
print(parts)