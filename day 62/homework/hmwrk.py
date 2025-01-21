# def is_valid_IP(strng):
#     luka = strng.split('.')
#     if len(luka) != 4:
#         return False
    
#     for octet in luka:
#         if not octet.isdigit():
#             return False
#         num = int(octet)
#         if num < 0 or num > 255:
#             return False
#         if octet != str(num):
#             return False
    
#     return True



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