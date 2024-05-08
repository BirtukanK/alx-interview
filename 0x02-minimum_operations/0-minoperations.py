#!/usr/bin/python3
'''defines minimum operations'''


from typing import List


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations
    using the operations 'Copy All' and 'Paste'.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required
    """
    if n == 1:
        return 0  # No operations needed if n is 1 (already 'H')

    dp: List[int] = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 character ('H') requires 0 operations

    # Simulate the process of generating characters from 1 to n
    for i in range(2, n + 1):
        # Try all possible factors of i (j) such that i % j == 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                if i // j != i and i // j != j:
                    dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n] if dp[n] != float('inf') else 0
