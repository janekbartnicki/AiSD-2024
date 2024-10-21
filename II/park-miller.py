def park_miller(x0, a, n, m = 10):
    results = []

    for _ in range(n):
        x0 = (a * x0) % m
        results.append(x0)

    return results


print(park_miller(1, 123123, 10, 5124124))
