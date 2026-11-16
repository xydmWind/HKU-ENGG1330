def digit_sum(n):
    if n < 10:
        return n
    else:
        return digit_sum(n // 10) + (n % 10)


n = int(input())
print(digit_sum(n))