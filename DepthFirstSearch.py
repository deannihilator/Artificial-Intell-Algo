visited = set()  # This is an empty set that will keep track of visited nodes.

graph = {  # This dictionary represents the graph structure.
    '5': ['3', '7'],  # Node 5 is connected to nodes 3 and 7.
    '3': ['2', '4'],  # Node 3 is connected to nodes 2 and 4.
    '7': ['8'],       # Node 7 is connected to node 8.
    '2': [],          # Node 2 has no outgoing connections.
    '4': ['8'],       # Node 4 is connected to node 8.
    '8': []           # Node 8 has no outgoing connections.
}

def dfs(visited, graph, node):
    if node not in visited:  # If the current node has not been visited yet.
        print(node)  # Print the current node.
        visited.add(node)  # Mark the current node as visited.

        for neighbour in graph[node]:  # For each neighbour of the current node.
            dfs(visited, graph, neighbour)  # Recursively call dfs on the neighbour.

print("The depth first search is: ")
dfs(visited, graph, '5')  # Start the depth-first search from node '5'.
