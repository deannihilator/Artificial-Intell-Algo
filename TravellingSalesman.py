import itertools

def tsp(graph):
    # Initialize the minimum cost as infinity and the optimal path as None.
    m_cost = float('inf')
    opt_path = None
    
    # Iterate through all possible permutations of nodes in the graph.
    for path in itertools.permutations(graph.keys()):
        # Calculate the cost of the current path by summing the edge costs.
        cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        cost += graph[path[-1]][path[0]]  # Add the cost of returning to the starting node.
        
        # Update the minimum cost and optimal path if the current path is better.
        if cost < m_cost:
            m_cost = cost
            opt_path = path
            
    return opt_path, m_cost

if __name__ == "__main__":
    graph = { 
        'a': {'b': 10, 'c': 15, 'd': 20},
        'b': {'a': 10, 'c': 35, 'd': 25},
        'c': {'a': 15, 'b': 35, 'd': 30},
        'd': {'a': 20, 'b': 25, 'c': 30}
    } 
    opt_path, m_cost = tsp(graph)
    print(f'Optimal path: {opt_path}')
    print(f"Minimum cost: {m_cost}")
