transaction_list = [
    "01-Oct/Food/15.50",
    "02-Oct/Gas/40.00",
    "03-Oct/Food/12.25",
    "04-Oct/Rent/800.00",
    "05-Oct/Gas/35.00",
    "05-Oct/Food/8.75"
]
def group_expenses(transaction_list):
    expense_dict = {}
    for i in transaction_list:    
        date, category, cost_str = i.split("/")
        cost = float(cost_str)
        if category in expense_dict:
            expense_dict[category].append((date, cost))
        else:
            expense_dict[category] = [(date, cost)]
    return expense_dict

def summarize_budget(expense_dict):
    for category, transactions in expense_dict.items():
        total_cost = 0
        for _, cost in transactions:
            total_cost += cost
        print(f"{category}: ${total_cost:.2f} total")

grouped_data = group_expenses(transaction_list)
summarize_budget(grouped_data)