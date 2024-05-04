#!/usr/bin/python3
''' Defines lockboxes algorithm'''


def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return False
    
    visited = set()
    to_visit = [0]
    visited.add(0)
    
    while to_visit:
        current_box = to_visit.pop(0)
        keys = boxes[current_box]
        
        for key in keys:
            if key < n and key not in visited:
                visited.add(key)
                to_visit.append(key)
    
    return len(visited) == n
