# def high(x):
#     alphabet = "|ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    
#     words = x.split()
    
#     scores = []
    
#     for word in words:
#         score = 0
#         for char in word:
#             score += alphabet.index(char)
#         scores.append(score)
    
#     max_score = max(scores)
#     max_word = scores.index(max_score)    
    
#     return words[max_word]


# def even_fib(n):
#     a, b = 0, 1  
#     even_sum = 0  
    
#     while a < n:
#         if a % 2 == 0: 
#             even_sum += a
#         a, b = b, a + b 
    
#     return even_sum\


# def array_diff(a, b):
#     filtered_arr = []
    
#     for element in a:
#         if element not in b:
#             filtered_arr.append(element)
    
#     return filtered_arr


# def bouncing_ball(h, bounce, window):
#     if h > 0 and bounce > 0 and bounce < 1 and window < h:
#         pass
#     else:
#         return -1
    
#     count = 0
    
#     while h > window:
#         count += 2
#         h = h * bounce
    
#     return count - 1



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