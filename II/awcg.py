def awcg(seed, j, k, n, m = 10):
    if j > k:
        j, k = k, j

    carry = 0
    results = []

    for _ in range(n):
        result = (seed[j] + seed[k] + carry) % m
        seed = seed[1:] + [result]
        results.append(result)

        if seed[j] + seed[k] + carry >= result:
            carry = 1
        else:
            carry = 0

    return results


k=5
seed=[i for i in range(k + 1)]

print(awcg(seed, 3, k, 10))