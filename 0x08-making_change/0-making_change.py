#!/usr/bin/python3
"""
making_change file
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed
    to meet a given amount total

    Return:
    fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins
            return -1
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    change = 0
    for coin in coins:
        while total - coin >= 0:
            change += 1
            total -= coin
    return change if total == 0 else -1
