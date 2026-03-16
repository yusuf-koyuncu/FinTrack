import json
import os
from typing import Dict, Any

class FinanceManager:
    def __init__(self):
        self.file_name = "data.json"
        self.transactions = self.load_data()

    def load_data(self):
        """Load transactions from JSON file."""
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_data(self):
        """Save transactions to JSON file."""
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.transactions, f, ensure_ascii=False, indent=4)

    def add_entry(self, title, amount, category, entry_type):
        """Add a new transaction to the records."""
        entry = {
            "title": title.title(), 
            "amount": float(amount), 
            "category": category.title(), 
            "type": entry_type
        }
        self.transactions.append(entry)
        self.save_data()

    def list_transactions(self):
        """Display all transactions in a professional table format."""
        if not self.transactions:
            print("\n⚠️ No records found.")
            return

        print("\n" + "="*65)
        print(f"{'TYPE':<10} | {'DESCRIPTION':<20} | {'CATEGORY':<14} | {'AMOUNT':<10}")
        print("-" * 65)
        
        for t in self.transactions:
            t_type = "INCOME" if t['type'] == 'income' else "EXPENSE"
            print(f"{t_type:<10} | {t['title']:<20} | {t['category']:<14} | {t['amount']:<10.2f} USD")
        print("="*65)

    def get_summary(self) -> Dict[str, Any]:
        """Calculate financial summary and category-based expense analytics."""
        income = sum(float(t.get('amount', 0)) for t in self.transactions if t.get('type') == 'income')
        expense = sum(float(t.get('amount', 0)) for t in self.transactions if t.get('type') == 'expense')
        
        # Category analytics for expenses
        expense_analytics: Dict[str, float] = {}
        for t in self.transactions:
            if t.get('type') == 'expense':
                cat = str(t.get('category', 'Unknown'))
                amt = float(t.get('amount', 0.0))
                expense_analytics[cat] = expense_analytics.get(cat, 0.0) + amt
                
        return {
            "total_income": income, 
            "total_expense": expense, 
            "balance": income - expense,
            "expenses_by_category": expense_analytics
        }

def main():
    manager = FinanceManager()
    
    while True:
        print("\n💰 FINTRACK v1.0 | 1. Add Income | 2. Add Expense | 3. List All | 4. Summary | 5. Exit")
        choice = input("Select an option: ").strip()
        
        if choice in ["1", "2"]:
            entry_type = "income" if choice == "1" else "expense"
            title = input("Description: ").strip()
            
            # Error Handling for Amount Input
            while True:
                try:
                    amount = float(input("Amount: ").strip())
                    if amount <= 0:
                        print("⚠️ Amount must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("⚠️ Invalid input! Please enter a valid number (e.g. 50 or 50.50).")
            
            category = input("Category: ").strip()
            manager.add_entry(title, amount, category, entry_type)
            print("✅ Transaction saved successfully.")
            
        elif choice == "3":
            manager.list_transactions()
            
        elif choice == "4":
            s = manager.get_summary()
            print(f"\n📊 FINANCIAL SUMMARY")
            print(f"Total Income  : {s['total_income']:.2f} USD")
            print(f"Total Expense : {s['total_expense']:.2f} USD")
            print(f"Net Balance   : {s['balance']:.2f} USD")
            
            # Category Analytics Display
            if s["expenses_by_category"]:
                print("\n📉 EXPENSE ANALYTICS BY CATEGORY")
                print("-" * 45)
                # Sort categories by amount (highest first)
                sorted_cats = sorted(s["expenses_by_category"].items(), key=lambda x: x[1], reverse=True)
                for cat, amt in sorted_cats:
                    percentage = (amt / s['total_expense']) * 100 if s['total_expense'] > 0 else 0
                    print(f" {cat:<15}: {amt:>8.2f} USD  (%{percentage:>04.1f})")
                print("-" * 45)
            
        elif choice == "5":
            print("Exiting FinTrack. Stay financially smart! 👋")
            break
            
        else:
            print("⚠️ Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()