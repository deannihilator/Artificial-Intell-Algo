# List of colors to choose from
colors = ['Yellow', 'Blue', 'Red']

# List of states that need to be colored
states = ['Andhara', 'Karnataka', 'TN', 'Kerala']

# Dictionary defining the neighbors of each state
neighbours = {
    'Andhara': ['Karnataka', 'TN'],
    'Karnataka': ['Andhara', 'TN', 'Kerala'],
    'TN': ['Andhara', 'Karnataka', 'Kerala'],
    'Kerala': ['Karnataka', 'TN']
}

# Dictionary to store the assigned color for each state
state_color = {}

# Iterate over each state to assign a color
for state in states:
    # Find the first available color that is not used by any neighboring state
    state_color[state] = next(color for color in colors
                              if all(color != state_color.get(neighbour)
                                     for neighbour in neighbours[state]))

# Print the resulting color assignment for each state
print(state_color)
