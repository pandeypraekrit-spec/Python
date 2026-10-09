cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

unique_cart = list(dict.fromkeys(cart))

print(unique_cart)
cart.append("Cheese") 
del cart[3]
cart.sort()
print("Final cart:", cart)
print("Total unique items:", len(cart))