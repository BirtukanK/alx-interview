#!/usr/bin/python3
'''defines minimum operations'''


from typing import List

def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters
    using the operations 'Copy All' and 'Paste'.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required. If achieving exactly n 'H' characters
             is impossible, return 0.
    """
    if n == 1:
        return 0  # No operations needed if n is 1 (already 'H')

    # Initialize a list to store the minimum operations required to have i characters
    dp: List[int] = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 character ('H') requires 0 operations

    # Simulate the process of generating characters from 1 to n
    for i in range(2, n + 1):
        # Try all possible factors of i (j) such that i % j == 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                # If j is a factor, we can generate i characters from j characters
                dp[i] = min(dp[i], dp[j] + (i // j))
                # If i/j is another valid factor, calculate operations accordingly
                if i // j != i and i // j != j:
                    dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n] if dp[n] != float('inf') else 0
