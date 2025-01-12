import heapq


def heap_sort(arr):
    max_heap = []
    result = []

    for element in arr:
        heapq.heappush(max_heap, (element))

    for _ in arr:
        result.append(heapq.heappop(max_heap))

    return result


print(heap_sort([3, 1, 55, 21, 2]))