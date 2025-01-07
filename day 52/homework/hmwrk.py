# def multiple_of_index(arr):
#     result = []
    
#     for i in range(len(arr)):
#         if i != 0:  
#             if arr[i] % i == 0:
#                 result.append(arr[i])
    
#     return result

# def gimme(triplet):
#     sorted_triplet = sorted(triplet)
#     middle_value = sorted_triplet[1]
#     return triplet.index(middle_value)

# def sum_of_minimums(numbers):
#     total_sum = 0
    
#     for row in numbers:
#         total_sum += min(row)
    
#     return total_sum


# def two_oldest_ages(ages):
#     unique_ages = list(set(ages))
#     unique_ages.sort(reverse=True)

#     if len(unique_ages) > 1:
#         return [unique_ages[1], unique_ages[0]]
#     else:
#         return [unique_ages[0], unique_ages[0]]



# def eve_fib(n):
#     fib_numbers = [0, 1]
    
#     while True:
#         next_fib = fib_numbers[-1] + fib_numbers[-2]
#         if next_fib >= n:
#             break
#         fib_numbers.append(next_fib)
    
#     even_sum = sum(num for num in fib_numbers if num % 2 == 0)
    
#     return even_sum