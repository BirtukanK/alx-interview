#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """ calculates perimeter of an island
    grid 2d matrix which reperesent 1 for land
    and 0 for water
    """
    p = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    p += 1
                if i == row - 1 or grid[i+1][j] == 0:
                    p += 1
                if j == 0 or grid[i][j-1] == 0:
                    p += 1
                if j == col-1 or grid[i][j+1] == 0:
                    p += 1
    return p
