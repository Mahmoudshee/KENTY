class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title_line = f"{self.category:*^30}\n"
        items = "".join(f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n" for item in self.ledger)
        total_line = f"Total: {self.get_balance():.2f}"
        return title_line + items + total_line


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    
    # Calculate spending percentage for each category
    spending_percentages = [
        (sum(item['amount'] for item in category.ledger if item['amount'] < 0) / category.get_balance()) * 100
        if category.get_balance() != 0
        else 0
        for category in categories
    ]

    # Create the chart
    for i in range(100, -1, -10):
        chart += f"{i:3}| " + " ".join("o" if percentage >= i else " " for percentage in spending_percentages) + " \n"

    chart += "    -" + "---" * len(categories) + "\n"

    # Write category names vertically
    max_name_length = max(len(category.category) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            chart += category.category[i] if i < len(category.category) else " "
            chart += "  "
        chart += "\n"

    return chart.rstrip()


# Example Usage
food_category = Category("Food")
clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
clothing_category.deposit(500, "initial deposit")
clothing_category.transfer(50, food_category)
entertainment_category.withdraw(15.89, "restaurant and more foo")

# Print individual categories
print(food_category)
print(clothing_category)
print(entertainment_category)

# Print spending chart
categories_list = [food_category, clothing_category, entertainment_category]
print(create_spend_chart(categories_list))
