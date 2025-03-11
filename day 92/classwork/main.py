# def collatz_length(n):
#     length = 1  
#     while n != 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3 * n + 1
#         length += 1
#     return length

# def longest_collatz(arr):
#     longest_num = arr[0]
#     longest_seq_length = collatz_length(arr[0])
    
#     for num in arr[1:]:
#         current_length = collatz_length(num)
#         if current_length > longest_seq_length:
#             longest_seq_length = current_length
#             longest_num = num
    
#     return longest_num

