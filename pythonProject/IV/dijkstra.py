import heapq


def dijkstra(graph, starting_node):
    min_heap = [(0, starting_node)]
    visited_nodes = set()
    result = 0

    for neighbor, weight in graph[starting_node].items():
        heapq.heappush(min_heap, (weight, neighbor))

    while min_heap:
        min_node_weight, min_node_name = heapq.heappop(min_heap)

        if min_node_name in visited_nodes:
            continue

        visited_nodes.add(min_node_name)
        result = max(result, min_node_weight)

        for node, weight in graph[min_node_name].items():
            if node not in visited_nodes:
                heapq.heappush(min_heap, (weight + min_node_weight, node))

    return result


graph = {
    'X': {'Y': 2, 'Z': 4},
    'Y': {'X': 2, 'Z': 1, 'W': 7},
    'Z': {'X': 4, 'Y': 1, 'W': 3, 'V': 5},
    'W': {'Y': 7, 'Z': 3, 'V': 1},
    'V': {'Z': 5, 'W': 1}
}

print(f'Koszt: {dijkstra(graph, 'X')}')