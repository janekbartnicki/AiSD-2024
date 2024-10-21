def lfg(j, k, n, seed_array, m = 10):
    if j > k:
        k, j = j, k
    results = []

    for i in range(n):
        result = (seed_array[j] + seed_array[k]) % m
        seed_array = seed_array[1:] + [result]
        results.append(result)

    return results


k = 10
seed_array = [i for i in range(k + 1)]

print(lfg(1, k, 10, seed_array))