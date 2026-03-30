products={
    "Pen":20,
    "Notebook":30,
    "Pencil":10
}

categories={"stationary","school items"}

product_details=[
    ("Pen",20),
    ("Note book",30),
    ("Pencil",10)
]

cart=[]

#function to display products

def display_products():
    print("Products Available")
    for product,price in products.items():
        print (product, ":" , price)

# to add items to cart
def add_Tocart():
    try:
        name=input("Enter product name: ")
        if name not in products:
            raise NameError
        qty=int(input("Enter quantity: "))
        cart.append((name,qty))
        print("Item added successfully")
    except ValueError:
        print("Invalid quantity, enter a number ")
    except NameError:
        print("product not found in store")
    except TypeError:
        print("cart data type error")

# to calculate total
def calculate_total(cart_lists,index=0):
    try:
        if index==len(cart_lists):
            return 0
        item,qty=cart_lists[index]
        price=products[item]
        return price * qty + calculate_total(cart_lists,index+1)
    except ZeroDivisionError:
        print ("Calculation error: division by zero")
        return 0
    except TypeError:
        print("Cart data type error")
        return 0
#view total bill
def view_total():
    print("items in cart")
    for item,qty in cart:
        print(item, "x", qty)
    total=calculate_total(cart)
    print("Total Bill: ",total)



while True:
    print("Product details of a store")
    print("1.Dispaly products")
    print("2. Add Items to cart")
    print("3.View Total Bill")
    print("4.Exit")

    choice=input("Enter your choice: ")

    if choice== "1":
        display_products()
    elif choice=="2":
        add_Tocart()
    elif choice =="3":
        view_total()
    elif choice=="4":
        print("Thank You ! for Shopping")
        break 
    else:
        print("Invalid choice")