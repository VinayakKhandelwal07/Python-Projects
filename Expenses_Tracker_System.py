import json
from tabulate import tabulate
from fpdf import FPDF

print("\n -------Welcome To Expense Tracking System-------")
class ExpenseTracker:
    def __init__(self):
        self.expenses = [] 

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
        else:
            table = [[i + 1, f"₹{e['amount']:.2f}", e['category']] for i, e in enumerate(self.expenses)]
            headers = ["Index", "Amount", "Category"]
            print(tabulate(table, headers, tablefmt="grid"))

    def view_spending_pattern(self, category=None):
        if category:
            expenses = [e['amount'] for e in self.expenses if e['category'] == category]
            total = sum(expenses)
            print(f"Total spending in '{category}': ₹{total:.2f}")
        else:
            total = sum(e['amount'] for e in self.expenses)
            print(f"Total spending across all categories: ₹{total:.2f}")

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed_expense = self.expenses.pop(index)
            print(f"Removed expense: Amount: ₹{removed_expense['amount']:.2f}, Category: {removed_expense['category']}")
        else:
            print("Invalid index. No expense removed.")

    def update_expense(self, index, amount=None, category=None):
        if 0 <= index < len(self.expenses):
            if amount is not None:
                self.expenses[index]['amount'] = amount
            if category is not None:
                self.expenses[index]['category'] = category
            print("Expense updated successfully!")
        else:
            print("Invalid index. No expense updated.")

    def view_total_spending(self):
        total = sum(e['amount'] for e in self.expenses)
        print(f"Total spending across all categories: ₹{total:.2f}")

    def view_category_wise_spending(self):
        category_totals = {}
        for e in self.expenses:
            if e['category'] in category_totals:
                category_totals[e['category']] += e['amount']
            else:
                category_totals[e['category']] = e['amount']
        table = [[category, f"${total:.2f}"] for category, total in category_totals.items()]
        headers = ["Category", "Total Spending"]
        print(tabulate(table, headers, tablefmt="grid"))
        

    def export_expenses_to_txt(self, filename):
        with open(filename, 'w') as file:
            for e in self.expenses:
                file.write(f"Amount: ${e['amount']:.2f}, Category: {e['category']}\n")
        print(f"Expenses exported to {filename}")

    def export_expenses_to_pdf(self, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Expense Report", ln=True, align='C')

        for i, e in enumerate(self.expenses):
            pdf.cell(200, 10, txt=f"{i + 1}. Amount: ${e['amount']:.2f}, Category: {e['category']}", ln=True)

        pdf.output(filename)
        print(f"Expenses exported to {filename}")

    def import_expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
            print(f"Expenses imported from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"File {filename} is not a valid JSON file.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
 


    while True:
        
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. Remove Expense")
        print("5. Update Expense")
        print("6. View Total Spending")
        print("7. View Category-wise Spending")
        print("8. Export Expenses to TXT File")
        print("9. Export Expenses to PDF File")
        print("10. Import Expenses from File")
        print("11. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the expense amount: ₹ "))
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully!")

        elif choice == 2:
            print("\nAll Expenses:")
            tracker.view_expenses()

        elif choice == 3:
            category = input("Enter the category to view spending pattern (leave blank for all): ")
            tracker.view_spending_pattern(category if category else None)

        elif choice == 4:
            tracker.view_expenses()
            index = int(input("Enter the index of the expense to remove: ")) - 1
            tracker.remove_expense(index)

        elif choice == 5:
            tracker.view_expenses()
            index = int(input("Enter the index of the expense to update: ")) - 1
            amount = input("Enter the new amount (leave blank to keep current): ")
            amount = float(amount) if amount else None
            category = input("Enter the new category (leave blank to keep current): ")
            category = category if category else None
            tracker.update_expense(index, amount, category)

        elif choice == 6:
            tracker.view_total_spending()

        elif choice == 7:
            tracker.view_category_wise_spending()

        elif choice == 8:
            filename = input("Enter the filename to export expenses (e.g., expenses.txt): ")
            tracker.export_expenses_to_txt(filename)

        elif choice == 9:
            filename = input("Enter the filename to export expenses (e.g., expenses.pdf): ")
            tracker.export_expenses_to_pdf(filename)

        elif choice == 10:
            filename = input("Enter the filename to import expenses: ")
            tracker.import_expenses(filename)

        elif choice == 11:
            print("Thank you ! Exiting...")
            break

        else:
            print("OOPS! Invalid choice")

        print("\nAction completed. Please select your next task from the menu below:\n")
