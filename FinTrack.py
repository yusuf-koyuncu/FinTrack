import json
import os

class FinanceManager:
    def __init__(self):
        self.file_name = "data.json"
        self.transactions = self.load_data()

    def load_data(self):
        """Load transactions from JSON file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_data(self):
        """Save transactions to JSON file."""
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.transactions, f, ensure_ascii=False, indent=4)

    def add_entry(self, title, amount, category, entry_type):
        entry = {
            "title": title, 
            "amount": float(amount), 
            "category": category, 
            "type": entry_type
        }
        self.transactions.append(entry)
        self.save_data()

    def list_transactions(self):
        """Display all transactions in a professional table format."""
        if not self.transactions:
            print("\n⚠️ No records found.")
            return

        print("\n" + "="*60)
        print(f"{'TYPE':<10} | {'DESCRIPTION':<20} | {'CATEGORY':<12} | {'AMOUNT':<10}")
        print("-" * 60)
        
        for t in self.transactions:
            t_type = "INCOME" if t['type'] == 'income' else "EXPENSE"
            print(f"{t_type:<10} | {t['title']:<20} | {t['category']:<12} | {t['amount']:<10.2f} USD")
        print("="*60)

    def get_summary(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expense = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return {"total_income": income, "total_expense": expense, "balance": income - expense}

def main():
    manager = FinanceManager()
    while True:
        print("\n💰 FINTRACK v1.0 | 1. Add Income | 2. Add Expense | 3. List All | 4. Summary | 5. Exit")
        choice = input("Select an option: ")
        
        if choice in ["1", "2"]:
            entry_type = "income" if choice == "1" else "expense"
            title = input("Description: ")
            amount = input("Amount: ")
            category = input("Category: ")
            manager.add_entry(title, amount, category, entry_type)
            print("✅ Transaction saved successfully.")
            
        elif choice == "3":
            manager.list_transactions()
            
        elif choice == "4":
            s = manager.get_summary()
            print(f"\n📊 FINANCIAL SUMMARY")
            print(f"Total Income  : {s['total_income']} USD")
            print(f"Total Expense : {s['total_expense']} USD")
            print(f"Net Balance   : {s['balance']} USD")
            
        elif choice == "5":
            print("Exiting FinTrack. Stay financially smart! 👋")
            break

if __name__ == "__main__":
    main()