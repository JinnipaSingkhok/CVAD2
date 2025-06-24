#starndard form
names = ['A', 'B', 'C']
scores = [85, 90, 95]
result = []
for i in range(len(names)):
    result.append((names[i], scores[i]))
print(result)

#zip form
#Syntax : zip(iterable1, iterable2, ...)
names = ['A', 'B', 'C']
scores = [85, 90, 95]
result = list(zip(names, scores))
print(result)