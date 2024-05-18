def sol_maze(maze, x=0, y=0):
    if x == y == len(maze) - 1:  # If the current position is at the bottom right corner (destination), return [(x, y)].
        return [(x, y)]
    
    # Check if the current position (x, y) is within the maze boundaries and is a valid path (maze[x][y] == 1).
    if 0 <= x < len(maze) and 0 <= y < len(maze) and maze[x][y] == 1:
        # Recursive step: Try moving right (x + 1, y) and down (x, y + 1) from the current position.
        return [(x, y)] + (sol_maze(maze, x + 1, y) or sol_maze(maze, x, y + 1))
    
    return []  # If the current position is not valid or if no path is found, return an empty list.

# Define the maze as a 2D list where 1 represents a valid path and 0 represents a blocked path.
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

# Call the sol_maze function to find a solution path through the maze.
solution = sol_maze(maze)

# Print whether a solution path is found or not.
print("Path found:" if solution else "No Solution Found!")

# If a solution path is found, print the coordinates of the path.
for x, y in solution:
    print(f"({x}, {y})")
