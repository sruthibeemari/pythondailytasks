#second largest in the list
numbers=[7,4,5,8,9]
numbers.sort()
print(numbers[-2])

# using loop

numbers = [7,4,5,8,3,9]
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num > largest:
        second =  largest
        largest = num
    elif num > second and num != largest:
        second=num 
print(second)


