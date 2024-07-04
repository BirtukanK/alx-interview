#!/usr/bin/python3
''' prime game'''


def sieve(n):
    '''filters which is the smallest'''
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p] is True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = []
    for p in range(2, n + 1):
        if is_prime[p]:
            prime_list.append(p)
    return prime_list


def prime_game(n):
    ''' prime game'''
    primes = sieve(n)
    remaining = set(range(1, n + 1))
    turn = 0  # Maria is 0, Ben is 1

    while True:
        found_prime = False
        for prime in primes:
            if prime in remaining:
                found_prime = True
                break
        if not found_prime:
            return "Ben" if turn == 0 else "Maria"

        remaining -= set(range(prime, n + 1, prime))
        turn = 1 - turn


def isWinner(x, nums):
    ''' checks who the winner is'''
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = prime_game(n)
            if winner == "Maria":
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
