# def valid_phone_number(phone_number):
#     splited_ph = phone_number.split()
#     if len(splited_ph) != 2 or phone_number.count("-") == 0:
#         return False
#     string1 = "()-0123456789"
#     if phone_number[0] != "(" or phone_number[4] != ")":
#         return False
#     elif len(splited_ph[1]) != 8:
#         return False
    
#     for i in "".join(splited_ph):
#         if i not in string1:
#             return False
#     return True


# def clean_string(s):
#     stack = []
    
#     for char in s:
#         if char == '#':
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(char)
            
#     return ''.join(stack)

# def highest_rank(arr):
#     frequency = []
#     max_freq = 0
#     result = arr[0]
    
#     for num in arr:
#         frequency[num] = frequency.get(num, 0) + 1
#         if frequency[num] > max_freq or (frequency[num] == max_freq and num > result):
#             max_freq = frequency[num]
#             result = num
            
#     return result