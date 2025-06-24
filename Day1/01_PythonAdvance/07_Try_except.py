#standard form
x = 0
if x != 0:
    result = 10 / x
    print(result)
else:
    print("Cannot divide by zero")

#try
try:
    result = 10 / 8
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")