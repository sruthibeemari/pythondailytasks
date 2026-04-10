data = [[1, 2, 3], [4, 5], [6]]
flatten=[i for sublist in data for i in sublist]
squares=[i*i for i in flatten if i%2==0]
print(flatten)
print("squares of even: ", squares)