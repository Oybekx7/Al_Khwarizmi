def calculate_bid(bid_text):
    subtotal = 0.0
    fee_rate = 0.0
    deposit = 0.0
    splitedbidtext = bid_text.split('\n')
    for a in splitedbidtext:
        if "FEE:" in a:
            clean_fee = a.replace("FEE:","").replace("%","").strip()
            clean_fee = float(clean_fee) / 100
            fee_rate = clean_fee
        elif "DEPOSIT:" in a:
            clean_deposit = a.replace("DEPOSIT:","").replace("$","").strip()
            deposit = float(clean_deposit)
        elif "->" in a:
            parts = a.split("->", 1)
            price_info = parts[1]
            price_parts = price_info.split("hrs at $")
            hours_str = price_parts[0].strip()
            hours = float(hours_str)
            rate_str = price_parts[1].replace("/hr", "").strip()
            rate = float(rate_str)
            subtotal += hours * rate
            
    fee_base = subtotal - deposit 
    grand_total = fee_base * (1 + fee_rate)

    return f"${grand_total:,.2f}"

bid1 = """Framing -> 10 hrs at $50.00/hr
Wiring -> 5 hrs at $80.00/hr
FEE: 10%
DEPOSIT: $100.00"""
print(calculate_bid(bid1))

bid2 = """Plumbing -> 2 hrs at $100.00/hr
Cleanup -> 1 hrs at $20.00/hr
FEE: 5%"""
print(calculate_bid(bid2))

bid3 = """Painting -> 4 hrs at $25.00/hr
Sanding -> 2 hrs at $15.00/hr
DEPOSIT: $30.00
FEE: 0%"""
print(calculate_bid(bid3))