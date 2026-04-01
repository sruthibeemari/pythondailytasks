file=open("grocery.txt","w")
while True:
    item=input("Enter grocery item (type 'stop to finish): ")
    if item.lower()=="stop":
        break
    file.write(item + "\n")

print("Grocery list saved to file")

file=open("grocery.txt","r")
print("\n Grocery list")
print(file.read())