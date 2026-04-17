cart=["Pen","Book","Pencil","Sketches","Bag","Pen","Book"]
cart_set=set(cart)

price={
    "Pen":30,
    "Book":20,
    "Pencil":10,
    "Sketches":40,
    "Bag":150
}

total=0
for i in cart_set:
    try:
        total+=price[i]
    except KeyError:
        print("Invalid Item",i)

print("Unique Items: ",cart_set)
print("Total Cost: ",total)
