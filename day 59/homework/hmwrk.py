# def lowercase_count(s):
#     count = 0
#     for char in s:
#         if char.islower():
#             count += 1
#     return count



# def digitize(n):
#     number_str = str(n)
#     digits = []
    
#     for char in number_str:
#         digit = int(char)
#         digits.append(digit)
    
#     reversed_digits = digits[::-1]
#     return reversed_digits

# def merge_arrays(arr1, arr2):
#     merged_array = arr1 + arr2
#     unique_sorted_array = sorted(set(merged_array))
#     return unique_sorted_array



# def collatz(n):
#     steps = 1 
#     while n != 1:
#         if n % 2 == 0: 
#             n = n // 2
#         else: 
#             n = 3 * n + 1
#         steps += 1 
#     return steps


# def DNA_strand(dna):
#     def complement_dna(dna):
#         complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     return ''.join([base] for base in dna)



# def swap_colons(strings):
#     first, second = strings
#     first_part, first_suffix = first.split(':')
#     second_part, second_suffix = second.split(':')
    
#     return [first_part + ':' + second_suffix, second_part + ':' + first_suffix]



# def team_weights(weights):
#     team1 = sum(weights[i] for i in range(0, len(weights), 2))
#     team2 = sum(weights[i] for i in range(1, len(weights), 2))
#     return (team1, team2)


# def mine_location(field):
#     for i in range(len(field)):
#         for j in range(len(field[i])):
#             if field[i][j] == 1:
#                 return [i, j]


def sum_of_digits(N):
    total_sum = 0
    for num in range(1, N + 1):
        total_sum += sum(int(digit) for digit in str(num))
    return total_sum