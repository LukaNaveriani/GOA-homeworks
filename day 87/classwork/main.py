# def missing_values(seq):
#     counts = {}
#     x = y = None
#     for num in seq:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1

#     for num, freq in counts.items():
#         if freq == 1:
#             x = num  
#         elif freq == 2:
#             y = num  

#     return x * x * y  


# def largest_pair_sum(numbers):
#     sorted_numbers = sorted(numbers, reverse=True)
#     return sorted_numbers[0] + sorted_numbers[1]



# def smaller(arr):
#     result = []
#     for i in range(len(arr)):
#         count = 0
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[i]:
#                 count += 1
#         result.append(count)
#     return result



# def transpose(matrix):
#     transposed_matrix = []

#     for col in range(len(matrix[0])):
#         transposed_row = []

#         for row in range(len(matrix)):
#             transposed_row.append(matrix[row][col])

#         transposed_matrix.append(transposed_row)

#     return transposed_matrix




# def square_sum(numbers):
#     sum=0
#     for i in numbers:
#         sum+=i**2
#     return sum