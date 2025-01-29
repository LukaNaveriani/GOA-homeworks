# def triple_double(num1, num2):
#     str_num1 = str(num1)
#     str_num2 = str(num2)

#     for digit in range(10):
#         digit_str = str(digit)
#         if str_num1.count(digit_str * 3) > 0:
#             if str_num2.count(digit_str * 2) > 0:
#                 return 1
#     return 0



# def pig_latin(word):
#     if not word.isalpha():
#         return None
    
#     word = word.lower()
    
#     if word[0] in 'aeiou':
#         return word + 'way'
    
#     for i, char in enumerate(word):
#         if char in 'aeiou':
#             return word[i:] + word[:i] + 'ay'
    
#     return word + 'ay'


