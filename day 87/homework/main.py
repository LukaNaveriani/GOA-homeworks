# def diamond(n):
#     if n <= 0 or n % 2 == 0:
#         return None
    
#     diamond_str = ""
    
#     for i in range(n // 2 + 1):
#         spaces = " " * (n // 2 - i)
#         stars = "*" * (2 * i + 1)
#         diamond_str += spaces + stars
    
#     for i in range(n // 2 - 1, -1, -1):
#         spaces = " " * (n // 2 - i)
#         stars = "*" * (2 * i + 1)
#         diamond_str += spaces + stars
    
#     return diamond_str



def matrix_addition(a, b):
    n = len(a)
    result = []
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    
    return result
