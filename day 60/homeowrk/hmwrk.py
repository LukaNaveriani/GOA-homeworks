# def greet(name):
#     capitalized_name = name.capitalize()
#     return "Hello " + capitalized_name + "!"


def generate_square(n):
    square_rows = []
    for i in range(n):
        row = "+" * n
        square_rows.append(row)
    square_shape = "\n".join(square_rows)
    return square_shape