def greedy_search(graph, start_node, goal_node):
    visited, path, current_node = set(), [], start_node

    while current_node != goal_node:
        path.append(current_node)
        visited.add(current_node)
        current_node = min(
            (neighbor for neighbor, cost in graph[current_node].items() if neighbor not in visited),
            key=lambda x: graph[current_node][x]
        )

    return path + [goal_node] if current_node == goal_node else None

# Example usage:
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4},
    'C': {'D': 7, 'E': 3},
    'D': {'E': 1, 'F': 2},
    'E': {'F': 6},
    'F': {}
}

start_node = 'A'
goal_node = 'F'
result = greedy_search(graph, start_node, goal_node)

print("Path:", result) if result else print("No path found")
