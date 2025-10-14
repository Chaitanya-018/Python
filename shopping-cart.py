from enum import nonmember

products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500}
]
cart = []

def viewProducts():
    print('--- Available Products ---')
    for p in products:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: {p['price']}")
    print('----------------------------')

def addToCart(products, cart, product_id, quantity):
    product=None           #Find the product in the products list
    for item in products:
        if item['id']==product_id:
            product=item
            break            #it will stop the iteration

    if not product:
        print("product not found")
        return      #it will end the function

    # If product already exists in cart, update its quantity and price
    for item in cart:
        if item['id']==product_id:
            item['quantity']+=quantity
            item['price'] = product['price'] * item['quantity']
            print(f" Updated {item['name']} in cart. New quantity: {item['quantity']}")
            viewCart()
            return

    # Otherwise, add as new item

    new_item = {
        "id": product["id"],
        "name": product["name"],
        "price": product["price"] * quantity,
        "quantity": quantity
    }
    cart.append(new_item)
    print(f"Added {new_item['name']} to cart for ₹{new_item['price']}")
    viewCart(cart)



def viewCart(cart):
    print('--- Your Cart ---')
    if not cart:
        print("cart is empty")
    else:
        for item in cart:
            print(f"ID: {item['id']} | Name: {item['name']} | Quantity: {item['quantity']} | Total Price: ₹{item['price']}")
        print('----------------------')

def updateCart(cart):
    if not cart:
        print("Cart is empty.")
        return

    id_to_update = int(input("Enter the ID to update: "))
    for item in cart:
        if item['id']==id_to_update:
            item['quantity'] += 1
            # Update price as well
            for p in products:
                if p["id"] == id_to_update:
                    item['price'] = p["price"] * item['quantity']
                    break
            print("✅ Item quantity updated successfully.")
            break
    else:
        print("Product not found in cart.")

def removeFromCart(cart):
    if not cart:
        print("Cart is empty.")
        return
    id_to_remove = int(input("Enter the ID to remove: "))

    for item in cart:
        if item['id']==id_to_remove:
            cart.remove(item)
            print(f"🗑 Removed {item['name']} from cart.")
            break

    else:
        print("Product not found in cart.")

def checkOut(cart):
    print('--- Checkout ---')
    total = sum(item['price'] for item in cart)
    print(f"Total Amount: ₹{total}")
    print("Thank you for shopping 🛍️")

while True:
    print('''
    1. View Products
    2. Add To Cart (example: add product id 1, quantity 2)
    3. View Cart
    4. Update Cart
    5. Remove From Cart
    6. Checkout''')

    ip = int(input("Enter choice: "))
    if ip == 1:
        viewProducts()

    elif ip == 2:
        pid = int(input("Enter product ID: "))
        qty = int(input("Enter quantity: "))
        addToCart(products, cart, pid, qty)

    elif ip == 3:
        viewCart(cart)

    elif ip == 4:
        updateCart(cart)

    elif ip == 5:
        removeFromCart(cart)

    elif ip == 6:
        checkOut(cart)
    else:
        print('Invalid option')



