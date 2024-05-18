from queue import PriorityQueue

def bfs(graph, start, goal):
    # Set to keep track of visited nodes
    visited = set()
    
    # PriorityQueue to prioritize nodes with the least cost
    pq = PriorityQueue()
    
    # Start with the initial node, with cost 0
    pq.put((0, start))
    
    while not pq.empty():
        # Get the node with the least cost
        cost, node = pq.get()
        
        # Mark the node as visited
        visited.add(node)
        
        # Print the current node
        print(node)
        
        # Check if the goal node is reached
        if node == goal:
            return True
        
        # Explore the neighbors of the current node
        for neighbour in graph[node]:
            if neighbour not in visited:
                # Add neighbors to the priority queue with their corresponding cost
                pq.put((graph[node][neighbour], neighbour))
    
    # Return False if the goal node is not reachable
    return False

# Define the graph as a dictionary
graph = {
    's': {'a': 12, 'b': 4},
    'a': {'c': 7, 'd': 3},
    'b': {'e': 8, 'f': 2},
    'e': {'g': 4},
    'f': {'h': 9, 'i': 0}
}

# Specify the start and goal nodes
start_node = 's'
goal_node = 'i'

# Call the BFS function and print if a path exists
path_exists = bfs(graph, start_node, goal_node)
print("Path exists: ", path_exists)
