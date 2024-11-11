# Products inventory with their Name, Price, and Quantity

products_inventory = {
    'handfree': {'Price': 475, 'Quantity': 306},
    'cable': {'Price': 200, 'Quantity': 5001}
}

# Displaying Inventory at the Start
print(products_inventory)

# This will continue to run until the user exits the application
while True:
    print("\nWelcome to the Products Inventory System")
    print("\nPress any number to perform the corresponding task:")
    print("1. For Adding a Product")
    print("2. For Updating any Product")
    print("3. For Deleting any Product")
    print("4. For Viewing any Product")
    print("5. For Counting Total Products")
    print("6. For Checking the Price of any Product")
    print("7. For Checking the Quantity of any Product")
    print("8. For Details of All Products with Price and Quantity")
    print("9. For Exiting the App")

    # Taking the task number from user and converting it into int
    task_num = int(input("\nEnter the number of the task you want to perform: "))

    # Perform task for input 1
    if task_num == 1:
        add_product_name = input("Enter the name of the product you want to add to the inventory: ").lower()
        if add_product_name in products_inventory: 
            print(f"The product {add_product_name} is already in the inventory.")
        else: 
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity of the product: "))

            products_inventory[add_product_name] = {'Price': price, 'Quantity': quantity}
            print(f"The product {add_product_name} has been added successfully.")

    # Perform task for input 2
    elif task_num == 2:
        update_product_name = input("Enter the name of the product you want to update: ").lower()
        if update_product_name in products_inventory:
            updated_price = int(input("Enter the updated price of the product: "))
            updated_quantity = int(input("Enter the updated quantity of the product: "))

            products_inventory[update_product_name] = {'Price': updated_price, 'Quantity': updated_quantity}
            print(f"\nThe product {update_product_name} has been updated successfully.")
        else:
            print(f"\nThe product {update_product_name} is not available in the inventory.")

    # Perform task for input 3
    elif task_num == 3:
        del_product = input("Enter the name of the product you want to delete: ").lower()
        if del_product in products_inventory:
            del products_inventory[del_product]
            print(f"The product {del_product} has been deleted successfully.")
            print(products_inventory)
        else:
            print(f"\nThe product {del_product} is not available in the inventory.")

    # Perform task for input 4
    elif task_num == 4:
        view_product = input("Enter the name of the product you want to view: ").lower()
        if view_product in products_inventory:
            print(f"The details of {view_product} are:")
            print(products_inventory[view_product])
        else:
            print(f"\nThe product {view_product} is not available in the inventory.")

    # Perform task for input 5
    elif task_num == 5:
        total_products = len(products_inventory)
        if total_products == 1:
            print("There is 1 product in the inventory.")
        else:
            print(f"There are {total_products} products in the inventory.")

    # Perform task for input 6
    elif task_num == 6:
        view_product_price = input("Enter the product for which you would like to know the price: ").lower()
        if view_product_price in products_inventory:
            price = products_inventory[view_product_price]['Price']
            print(f"The price of {view_product_price} is {price}.")
        else:
            print(f"\nThe product {view_product_price} is not available in the inventory.")

    # Perform task for input 7
    elif task_num == 7:
        quantity_view = input("Enter the product for which you would like to know the quantity: ").lower()
        if quantity_view in products_inventory:
            product_quantity = products_inventory[quantity_view]['Quantity']
            if product_quantity == 1:
                print(f"The quantity of {quantity_view} is {product_quantity}.")
            else:
                print(f"The quantity of {quantity_view} is {product_quantity}.")
        else:
            print(f"\nThe product {quantity_view} is not available in the inventory.")

     # Perform task for input 8
    elif task_num == 8:
        for products , details in products_inventory.items():
            print(f"\nProduct Name is:",products.capitalize())
            print(f"Price is {details['Price']}")
            print(f"Quantity is {details['Quantity']}")


    # Perform task for input 8 (Exit)
    elif task_num == 9:
        print("You have exited the app.\nTHANK YOU")
        break

    else:
        print("Please enter a valid task number.")