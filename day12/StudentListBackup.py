import copy
marks=[50, 60, 70, 80]
marks[0]=90
backup=copy.copy(marks)
print(marks)
print(backup)


# shallow copy refers nested objects so changes in nested objects reflects both copies