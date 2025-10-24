print("=== Pizza Shop Order System ===")
print("Enter pizza size: personal, medium, or family")
print("Type 'done' when finished ordering")

total = 0

while True:
    size = input("\nEnter pizza size: ").lower()
    if size == "done":
        break

    if size == "personal":
        price = 7.00
    elif size == "medium":
        price = 12.00
    elif size == "family":
        price = 18.00
    else:
        print("\nInvalid size! Please enter personal, medium, or family.\n")
        continue

    total += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")

print("\n===== Order Summary =====")
print(f"Subtotal: ${total:.2f}")

if total > 39:
   discount = 5.00 
else:
   discount = 0.00
final_total = total - discount

print(f"Party Order Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for your order!")