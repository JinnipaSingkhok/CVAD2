#standard form
nums = [1, 2, 3, 4]
evens = []
for x in nums:
    if x % 2 == 0:
        evens.append(x)
print(evens)

#filter form
#Syntax : filter(function, iterable)
nums = [1, 2, 3, 4]
evens = list(filter(lambda x:x % 2 == 0,nums))
print(evens)