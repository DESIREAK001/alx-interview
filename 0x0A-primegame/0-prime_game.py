#!/usr/bin/python3
"""
prime_game module
"""


def builPrimesArray(n):
    '''
        builds an array up to n where the index
        of prime numbers are set true and others to false
    '''
    if n <= 0:
        return []
    testArray = [True for i in range(n + 1)]
    testArray[0], testArray[1] = False, False
    i = 2
    while(i * i <= n):
        if testArray[i]:
            for j in range(i * i, n + 1, i):
                testArray[j] = False
        i += 1
    return testArray


def isWinner(x, nums):
    '''
        determins the winner betwent Maria and Ben in game
        of selecting prime numbers up to n for x round
    '''
    if x <= 0 or nums is None:
        return

    numsL = len(nums)
    primes = builPrimesArray(max(nums))
    Maria = 0
    Ben = 0
    for round in range(x):
        valid = [n for n in range(2, nums[round % numsL] + 1) if primes[n]]
        if len(valid) % 2 == 1:
            Maria += 1
        else:
            Ben += 1
    if Ben == Maria:
        return
    elif Ben > Maria:
        return 'Ben'
    else:
        return 'Maria'
