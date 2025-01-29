# def merge_strings(s1, s2):
#     max_overlap = 0
#     max_length = min(len(s1), len(s2))
    
#     for i in range(1, max_length + 1):
#         if s1[-i:] == s2[:i]:
#             max_overlap = i
            
#     return s1 + s2[max_overlap:]

# def reverse_it(data):
#     if type(data) == str:
#         return data[::-1]
#     elif type(data) == int:
#         return int(str(data)[::-1])
#     elif type(data) == float:
#         return float(str(data)[::-1])
#     return data


# def letter_range(range_str):
#     start_letter, end_letter = range_str.split('-')
#     letter_list = []
#     start_code = ord(start_letter)
#     end_code = ord(end_letter)
    
#     for code in range(start_code, end_code + 1):
#         letter_list.append(chr(code))
    
#     result = ''.join(letter_list)
#     return result


# def number(bus_stops):
#     people = 0  
    
#     for get_on, get_off in bus_stops:
#         people += get_on  
#         people -= get_off
#     return people


# def largest_pair_sum(numbers):
#     sorted_numbers = sorted(numbers, reverse=True)
#     return sorted_numbers[0] + sorted_numbers[1]



def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i+1]) != ord(chars[i]) + 1:
            return chr(ord(chars[i]) + 1)