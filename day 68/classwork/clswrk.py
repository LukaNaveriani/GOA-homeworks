# def dup(arry):
#     result = []
    
#     for word in arry:
#         changed_word = word[0]
#         for i in range(1, len(word)):
#             if word[i] != word[i-1]:
#                 changed_word += word[i]
#         result.append(changed_word)
        
#     return result


# def shortest_steps_to_num(num):
#     current_numbers = [(1, 0)]  
#     visited = set()  

#     while current_numbers:
#         current, steps = current_numbers.pop(0)

#         if current == num:
#             return steps
        
#         if current < num and current not in visited:
#             visited.add(current)
#             current_numbers.append((current + 1, steps + 1))
#             current_numbers.append((current * 2, steps + 1))
            


# n = 3
# result = []

# for i in range(1, n + 1):
#     result.append([1] * i)

# print(result)  