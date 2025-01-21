# def vowel_indices(word):
#     vowels = 'aeiouAEIOU'
#     indices = []
#     for i, char in enumerate(word, start=1):
#         if char in vowels:
#             indices.append(i)
#     return indices

# def prime_factors(n):
#     factors = []
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2
#     i = 3
#     while i * i <= n:
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#         i += 2
#     if n > 2:
#         factors.append(n)
#     return factors


# def more_zeros(s):
#     result = []
#     seen = set()
#     for char in s:
#         binary = bin(ord(char))[2:]  
#         if binary.count('0') > binary.count('1'):
#             if char not in seen:
#                 result.append(char)
#                 seen.add(char)
#     return result


from collections import Counter

def arrays_similar(arr1, arr2):

    if len(arr1) != len(arr2):
        return False

    count1 = Counter(arr1)
    count2 = Counter(arr2)


    return count1 == count2
