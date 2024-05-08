#!/usr/bin/python3
'''defines minimum operations'''


def minOperations(n):
    '''min operation method'''
    if n == 1:
        return 0  # No operations needed if n is 1 (already 'H')

    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 character ('H') requires 0 operations

    for i in range(2, n + 1):
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                if i // j != i and i // j != j:
                    dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n] if dp[n] != float('inf') else 0
