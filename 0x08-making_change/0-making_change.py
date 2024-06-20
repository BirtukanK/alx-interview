#!/usr/bin/python3
""" Making change"""


def makeChange(coins, total):
    """ make change method with
    coins - list of coins
    total - total amount to be achived
    """
    if total <= 0:
        return 0
    for value in coins:
        if value <= 0:
            return
    n = len(coins)
    ans = []
    i = n - 1
    while(i >= 0):
        while(total >= coins[i]):
            total = total - coins[i]
            ans.append(coins[i])
        i = i - 1
    if total != 0:
        return -1
    else:
        return len(ans)
