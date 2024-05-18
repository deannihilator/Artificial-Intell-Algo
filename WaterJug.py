from collections import defaultdict

jug1, jug2, aim = 4, 3, 2  # Jug capacities and the target amount of water to measure.
visited = defaultdict(lambda: False)  # A defaultdict to keep track of visited states.

def WaterJugSolver(X, Y):
    # Base case: If either jug1 or jug2 has the desired amount of water, print the state and return True.
    if (X == aim and Y == 0) or (Y == aim and X == 0):
        print(X, Y)
        return True
    
    # If the current state (X, Y) has not been visited yet.
    if visited[(X, Y)] == False:
        print(X, Y)
        visited[(X, Y)] = True  # Mark the current state as visited.

        # Try all possible operations to reach the target state.
        return (
            WaterJugSolver(0, Y) or  # Empty jug1.
            WaterJugSolver(X, 0) or  # Empty jug2.
            WaterJugSolver(jug1, Y) or  # Fill jug1 to capacity.
            WaterJugSolver(X, jug2) or  # Fill jug2 to capacity.
            WaterJugSolver(X + min(Y, (jug1 - X)), Y - min(Y, (jug1 - X))) or  # Pour water from jug2 to jug1.
            WaterJugSolver(X - min(X, (jug2 - Y)), Y + min(X, (jug2 - Y)))     # Pour water from jug1 to jug2.
        )

jug1, jug2, aim = 4, 3, 2  # Resetting the jug capacities and the target amount.
visited = defaultdict(lambda: False)  # Resetting the visited states.
print("Steps: ")
WaterJugSolver(0, 0)  # Start the Water Jug problem-solving from the initial state (0, 0).
