def lcg(x0, a, c, n, m = 10):
    result = x0
    results = []

    for _ in range(n):
        result = (a * result + c) % m
        results.append(result)

    return results


print(lcg(7, 5, 3, 10, 16))