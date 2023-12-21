from queue import PriorityQueue
def best_first_search(graph, start, goal, heuristic):
    queue = PriorityQueue()
    queue.put((heuristic[start], start))  # Enqueue the start node with its heuristic value
    visited = set()  # Set to keep track of visited nodes
    
    while not queue.empty():
        _, current = queue.get()  # Dequeue the node with the lowest priority
        
        if current == goal:
            return True  # Solution found
        
        visited.add(current)  # Mark the current node as visited
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                priority = heuristic[neighbor]  # Calculate the priority (heuristic value)
                queue.put((priority, neighbor))  # Enqueue the neighbor with its priority
        
    return False  # No solution found
# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
# Heuristic values for each node
heuristic = {
    'A': 10,
    'B': 5,
    'C': 8,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 6
}
start_node = 'A'
goal_node = 'G'
# Perform Best-First Search
result = best_first_search(graph, start_node, goal_node, heuristic)
# Print the result
if result:
    print("Goal reached!")
else:
    print("No solution found.")
