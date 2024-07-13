#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    checks if all boxes have keys
    """
    allboxes = len(boxes)
    explored = []
    keys = [0]

    while len(explored) != allboxes and len(keys) != 0:
        for key in boxes[keys[0]]:
            if key not in explored and key not in keys and key < allboxes:
                keys.append(key)
        explored.append(keys.pop(0))

    return len(explored) == allboxes
