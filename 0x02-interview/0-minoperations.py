#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
needed to achieve a specific number of 'H' characters using "Copy All" and "Paste"
operations.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed. If n is impossible to achieve,
         returns 0.
    """
    # If n is less than or equal to 0, return 0 as it's impossible to achieve
    if n <= 0:
        return 0

    operations = 0
    while n > 0:
        # If n is even, divide it by 2 (equivalent to "Copy All" operation)
        if n % 2 == 0:
            n //= 2
        # If n is odd, subtract 1 from n and increment operations by 1 (equivalent to "Paste" operation)
        else:
            n -= 1
            operations += 1

        operations += 1  # Increment operations for either action taken

    return operations

# Example usage
if __name__ == "__main__":
    import sys

    try:
        n = int(sys.argv[1])
        print(f"Min # of operations to reach {n} chars: {minOperations(n)}")
    except IndexError:
        print("Usage: python3 0-minoperations.py <number>")

