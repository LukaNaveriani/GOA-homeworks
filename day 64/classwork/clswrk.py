# def derive(coefficient, exponent):
#     new_coefficient = coefficient * exponent
#     new_exponent = exponent - 1
    
#     if new_exponent == 1:
#         return str(new_coefficient) + "x"
#     elif new_exponent == 0:
#         return str(new_coefficient)
#     else:
#         return str(new_coefficient) + "x^" + str(new_exponent)



# def add(a, b):
#     return a + b

# def subt(a, b):
#     return a - b

# def mod(a, b):
#     return a % b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a // b, a / b

# def exponent(a, b):
#     return a ** b



def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
