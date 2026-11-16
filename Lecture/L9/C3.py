def merge_readings(left, right):
    tmp_readings = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            tmp_readings.append(left[left_index])
            left_index += 1
        else:
            tmp_readings.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        tmp_readings.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        tmp_readings.append(right[right_index])
        right_index += 1

    return tmp_readings


n = int(input())
left = []
for i in range(n):
    left.append(int(input()))
m = int(input())
right = []
for i in range(m):
    right.append(int(input()))
print(merge_readings(left, right))
print(left)
print(right)