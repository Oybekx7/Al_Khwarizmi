print("=== Pizza Shop Order System ===")
print("Enter pizza size: personal, medium, or family")
print("Type 'done' when finished ordering")

total = 0

while True:
    size = input("Enter pizza size: ")
    if size == "done":
        break

    if size == "personal":
        prices = 7.00
    elif size == "medium":
        prices = 12.00
    elif size == "family":
        prices = 18.00
    else:
        print("Invalid size! Please enter personal, medium or family. \n")
        continue

    total += prices
    print(f"Price: ${prices:.2f}")
    print(f"Current total: ${total:.2f} \n")

discount = 0
if total > 39:
    discount = 5
final_total = total - discount 

print("=== Order Summary ===")
print(f"Subtotal: ${total:.2f}")
if discount > 0:
    print(f"Party Order Discount: -${discount:.2f}")
else:
    print(f"Party Order Discount: 0")
print(F"Final Total: ${final_total:.2f}")
print("Thank you your order!")