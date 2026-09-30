# A list of dictionaries representing products in a cart
shopping_cart = [
    {"item": "Laptop Sleeve", "price": 25.00, "quantity": 1},
    {"item": "Wireless Mouse", "price": 15.50, "quantity": 2},
    {"item": "HDMI Cable", "price": 8.00, "quantity": 3}
]

total_bill = 0.0

print("--- Your Order Receipt ---")
# Loop through the list to calculate totals
for product in shopping_cart:
    item_total = product["price"] * product["quantity"]
    total_bill += item_total
    print(f"{product['item']} x{product['quantity']}: ${item_total:.2f}")

print("-" * 26)
print(f"Total Amount Due: ${total_bill:.2f}")
