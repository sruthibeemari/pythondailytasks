#find an element exists in a tuple
mytuple=[3,4,5,6,7,8]
e=4
if e in mytuple:
    print(e,"exists in tuple")

#using loop
mytuple=[3,4,5,6,7,8]
element=int(input("enter a number: "))
found=False
for i in mytuple:
    if element==i:
        found=True
        break
if found==True:
    print(element,"exists in tuple")
else:
    print(element," not exists in tuple")
   