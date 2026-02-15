class MealCard:
    cafeteria_name = "Campus Cafe"
    min_balance = 5
    total_cards = 0

    def __init__(self, student, balance=0, transactions=None):
        self.student = student
        self.balance = balance
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions
        MealCard.total_cards += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            record = f"+{amount}"
            self.transactions.append(record)
            print(f"Deposited {amount}. Balance: {self.balance}")

    def purchase(self, amount):
        if self.balance - amount >= MealCard.min_balance:
            self.balance -= amount
            record = f"-{amount}"
            self.transactions.append(record)
            print(f"Purchased meal for {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance for purchase")

    def display_card(self):
        print(f"Student: {self.student}, Balance: {self.balance}, Cafeteria: {self.cafeteria_name}")

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)

student = MealCard("Malika", 15)
student.display_card()
student.deposit(30)
student.purchase(12)
student.purchase(10)
student.show_transactions()
print(f"Total cards: {MealCard.total_cards}")