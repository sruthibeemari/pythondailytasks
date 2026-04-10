import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
dcopy=copy.deepcopy(employees)
Scopy=copy.copy(employees)
employees[0][1]="Z"
print("Nested list :",employees)
print("Shallow Copy: ",Scopy)
print("Deep Copy: ",dcopy)

# shallow copy refers nested objects so changes in nested objects reflects both copies
# where as deep copy creates a completely independent copy.