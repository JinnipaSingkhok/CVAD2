#standard form
nums = [1, 2, 3, 4]
squared = []
for x in nums:
    squared.append(x ** 2)
print(squared)

#map form
#Syntax : map(function, iterable)
nums = [1, 2, 3, 4]
squared = list(map(lambda x:x**2,nums))
print(squared)