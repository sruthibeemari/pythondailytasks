# to check how many times an element appears in tuple
# mytuple=(1,3,2,3,4,3,6,7)
# element=3
# print("element repeated",mytuple.count(element),"times")

# using loop
mytuple=(1,3,2,3,4,3,6,7)
element=3
count=0
for i in mytuple:
    if element==i:
        count+=1
print("element appears",count,"times")
