import json

class BudgetTracker:
    def __init__(self, filename="budget.json"):
        self.filename = filename
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"income": 0, "expenses": []}

    def add_income(self, amount):
        self.data["income"] += amount
        self._save()

    def add_expense(self, name, amount):
        self.data["expenses"].append({"name": name, "amount": amount})
        self._save()

    def summary(self):
        total_expense = sum(x["amount"] for x in self.data["expenses"])
        balance = self.data["income"] - total_expense
        print(f"Total Income: {self.data['income']}")
        print(f"Total Expenses: {total_expense}")
        print(f"Balance: {balance}")

    def _save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=2)

# Example Usage
if __name__ == '__main__':
    tracker = BudgetTracker()
    tracker.add_income(1000)
    tracker.add_expense("Groceries", 150)
    tracker.add_expense("Internet", 50)
    tracker.summary()
