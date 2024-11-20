import heapq


def prim(graph, starting_node):
    graph_length = len(graph)
    visited_vertices = set()
    min_heap = []
    result = []

    for neighbor, weight in graph[starting_node].items():
        heapq.heappush(min_heap, (weight, neighbor))

    visited_vertices.add(starting_node)
    while len(visited_vertices) < graph_length:
        min_node = heapq.heappop(min_heap)

        if min_node not in visited_vertices:
            visited_vertices.add(min_node[1])
            result.append(min_node)

            for neighbor, weight in graph[min_node[1]].items():
                if neighbor not in visited_vertices:
                    heapq.heappush(min_heap, (weight, neighbor))

    return result


graph = {
    'A': {'B': 28, 'F': 10},
    'B': {'A': 28, 'C': 16, 'G': 14},
    'C': {'B': 16, 'D': 12},
    'D': {'C': 12, 'E': 22},
    'E': {'D': 22, 'F': 25, 'G': 24},
    'F': {'A': 10, 'E': 25},
    'G': {'B': 14, 'E': 24}
}

cost = 0
for weight, node in prim(graph, 'A'):
    print(node, end=" -> ")
    cost += weight

print(f'\n MST cost: {cost}')

