def repair_readings(readings):
    repaired_readings = readings[:]
    left = -1
    right = -1

    for start in range(len(readings)):
        if repaired_readings[start] != -1:
            left = repaired_readings[start]
            continue
        
        end = start
        for right_place in range(start, len(readings)):
            if repaired_readings[right_place] != -1:
                right = repaired_readings[right_place]
                break
            right = -1
            end += 1

        if left == -1:
            replacement = right
        elif right == -1:
            replacement = left
        else:
            replacement = (left + right) // 2
        for repaired_place in range(start, end):
            repaired_readings[repaired_place] = replacement

    return repaired_readings


if __name__ == "__main__":
    n = int(input())
    readings = [int(value) for value in input().split()]
    repaired = repair_readings(readings)
    print('Repaired:', *repaired)