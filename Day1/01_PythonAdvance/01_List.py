#Standard Form
squares = []
for i in range(5):
    squares.append(i**3)
print(squares)

#list form
squares = [x**3 for x in range(5)]
print(squares)
