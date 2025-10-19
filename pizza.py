print("=== Pizza Shop Order System ===")
print("Enter pizza size: personal, medium, or family")
print("Type 'done' when finished ordering")

total = 0

while True:
    size = input("\nEnter pizza size: ")
    if size == "done":
        break

    if size == "personal":
        prices = 7.00
    elif size == "medium":
        prices = 12.00
    elif size == "family":
        prices = 18.00
    else:
        print("\nInvalid size! Please enter personal, medium or family.\n")
        continue
    total += prices
    print(f"Price: ${prices:.2f}")
    print(f"Current total: ${total:.2f}")

print("\n=== Order Summary ===")
print(f"Subtotal: ${total:.2f}")
if total > 39:
    print(f"Party Order Discount: -$5.00")
else:
    print(f"Party Order Discount: $0.00")
if total > 39:
    print(f"Final Total: ${total - 5}")
else:
    print(f"Final Total: ${total}")
print("Thank you for your order!")