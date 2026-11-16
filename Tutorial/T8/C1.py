def filter_readings(values: list, lower: int, upper: int) -> list:
    tmp_values = []
    for value in values:
        if lower <= value <= upper:
            tmp_values.append(value)
    return tmp_values


def filter_readings_lambda(values: list, lower: int, upper: int) -> list:
    return list(filter(lambda value: lower <= value <= upper, values))


n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
lower = int(input())
upper = int(input())
print(filter_readings(values, lower, upper))
print(filter_readings_lambda(values, lower, upper))
print(values)