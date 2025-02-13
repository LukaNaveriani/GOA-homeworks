# def solve(s):
#     alphabet = "|ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    
#     s = s.replace("e", "a").replace("i", "a").replace("o", "a").replace("u", "a")
    
#     subs = s.split("a")
#     scores = []
    
#     for sub in subs:
#         score = 0
#         for char in sub:
#             score += alphabet.index(char)
#         scores.append(score)
    
#     return max(scores)

# def extract_numbers(input_string):
#     result = ""
#     for i in range(len(input_string)):  
#         if input_string[i].isdigit():  
#             result += input_string[i]  
#     return result


# from collections import Counter

# def most_frequent(arr):
#     count = Counter(arr)
#     most_frequent_num = max(count, key=lambda x: (count[x], x))
#     return most_frequent_num


def plus_one(arr):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    num = int(''.join(map(str, arr))) + 1
    return [int(digit) for digit in str(num)]