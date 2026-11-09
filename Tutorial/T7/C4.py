def record_reading(value: int, history=None) -> list:
    if history is None:
        history = []
    history.append(value)
    return history


x = int(input())
y = int(input())
z = int(input())
first = record_reading(x)
second = record_reading(y)
print(first)
print(second)
print(first is second)
result = record_reading(z, first)
print(first)
print(second)
print(result is first)