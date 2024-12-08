import heapq


def a_star(graph, heuristics, starting_node, finish_node):
    # (total_cost, cost_to_reach, node)
    min_heap = [(heuristics[starting_node], 0, starting_node)]

    cost_to_reach = { node: float('inf') for node in graph }
    cost_to_reach[starting_node] = 0

    came_from = {}

    while min_heap:
        current_total_cost, current_cost, current_node = heapq.heappop(min_heap)

        if current_node == finish_node:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(starting_node)
            return path[::-1]

        for neighbor, weight in graph[current_node].items():
            tentative_cost = current_cost + weight

            if tentative_cost < cost_to_reach[neighbor]:
                cost_to_reach[neighbor] = tentative_cost
                total_cost = tentative_cost + heuristics[neighbor]
                heapq.heappush(min_heap, (total_cost, tentative_cost, neighbor))
                came_from[neighbor] = current_node

    return None

graph = {
    'X': {'Y': 2, 'Z': 4},
    'Y': {'X': 2, 'Z': 1, 'W': 7},
    'Z': {'X': 4, 'Y': 1, 'W': 3, 'V': 5},
    'W': {'Y': 7, 'Z': 3, 'V': 1},
    'V': {'Z': 5, 'W': 1}
}

heuristics = {
    'X': 7,
    'Y': 6,
    'Z': 2,
    'W': 1,
    'V': 0
}

start = 'X'
goal = 'V'
print(a_star(graph, heuristics, start, goal))
