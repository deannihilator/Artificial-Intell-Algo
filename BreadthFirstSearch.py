# Define the graph as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Lists to keep track of visited nodes and the queue for BFS
visited = []
queue = []

# Function to perform BFS traversal
def bfs(visited, graph, node):
    # Start by visiting the initial node
    visited.append(node)
    queue.append(node)
    
    while queue:
        # Dequeue a node from the front of the queue
        m = queue.pop(0)
        print(m, end=" ")
        
        # Get all adjacent nodes of the dequeued node
        for neighbour in graph[m]:
            # If an adjacent node has not been visited, mark it as visited and enqueue it
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Print the BFS traversal
print("The breadth search is: ")
bfs(visited, graph, '5')
