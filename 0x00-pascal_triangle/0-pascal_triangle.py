#!/usr/bin/python3
""" pascal triangle"""
def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the Pascal's triangle list of lists
    triangle = [[1]]  # Start with the first row [1]

    for i in range(1, n):
        # Generate the next row based on the current row
        prev_row = triangle[-1]
        new_row = [1]  # The first element of each row is always 1

        # Calculate the values for the rest of the row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # The last element of each row is always 1
        triangle.append(new_row)  # Append the new row to the triangle

    return triangle

# Example usage and printing the triangle
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Test the pascal_triangle function with n = 5
    triangle = pascal_triangle(5)
    print_triangle(triangle)
