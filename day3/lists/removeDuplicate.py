#remove duplicate elements from list
numbers=[1,2,4,3,5,4,2,6,7]
remove_elements=set(numbers)
print(remove_elements)

#or
numbers=[1,2,4,3,5,4,2,6,7]
emptylist=[]
for i in numbers:
    if i not in emptylist:
        emptylist.append(i)
print(emptylist)


