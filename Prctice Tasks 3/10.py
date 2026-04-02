"""
Write a Python function that performs matrix multiplication using list comprehensions.
"""
def matrix_multiply(A, B):
    BT = list(zip(*B))
    
    result = [
        [sum(a * b for a, b in zip(row, col)) for col in BT]
        for row in A
    ]
    
    return result


A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

print(matrix_multiply(A, B))