def latin(n):
    k = n + 1  # Initialize a variable k as n + 1.
    
    # Iterate over the range from 1 to n, with a step size of 1.
    for i in range(1, n + 1, 1):
        temp = k  # Assign the value of k to a temporary variable temp.
        
        # While temp is less than or equal to n, print temp and increment temp by 1.
        while temp <= n:
            print(temp, end="")
            temp += 1
        
        # Iterate over the range from 1 to k-1.
        for j in range(1, k):
            print(j, end="")
        
        k -= 1  # Decrement k by 1.
        print()  # Move to the next line after each iteration of the outer loop.

n = int(input('Enter a number: '))  # Take user input for the number n.
latin(n)  # Call the latin function with the user-provided input.
