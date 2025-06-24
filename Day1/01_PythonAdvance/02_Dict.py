#standard form
even_squares = {}
for x in range(10):
    if x % 2 == 0:
        even_squares[x] = x**2
print(even_squares)

# Dict form
#Syntax : {key_expr: value_expr for item in iterable if condition}
even_squares = {x: x**2 for x in range(10) if x % 2 == 0 }
print(even_squares)