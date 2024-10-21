def fibonacci_random(x1, x2, n, m = 10):
    if n == 1:
        return 1
    if n == 0:
        return 0

    result = [x1, x2]
    for i in range(2, n):
        result.append((result[i - 1] + result[i - 2]) % m);

    return result


print(fibonacci_random(4, 7, 10))