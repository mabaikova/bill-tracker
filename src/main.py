from pathlib import Path
import pandas as pd
import json

def load_transactions(file_path):
    return pd.read_csv(file_path)

def validate_transactions(transactions):
    required = {"date", "description", "amount"}
    actual = set(transactions.columns)
    missing = required - actual

    if missing:
        raise ValueError(f"Missing required columns: {", ".join(sorted(missing))}")

def clean_transactions(transactions):
    transactions["date"] = pd.to_datetime(transactions["date"], format="%Y-%m-%d", errors="coerce")
    if transactions["date"].isna().any():
        raise ValueError("Invalid transaction date")
    transactions["description"] = transactions["description"].str.strip()
    if transactions["description"].isna().any() or (transactions["description"] == "").any():
            raise ValueError("Invalid transaction description")
    transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")
    if transactions["amount"].isna().any():
        raise ValueError("Invalid transaction amount")
    return transactions
<<<<<<< HEAD
                    
=======

def load_category_rules(rules_path):
    with open(rules_path, "r", encoding="utf-8") as file:
        rules = json.load(file)
        return rules

def save_category_rules(rules_path, rules):
    with open(rules_path, "w", encoding="utf-8") as file:
        json.dump(rules, file, indent=4)

def categorize_transaction(description, rules):
    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword.lower() in description.lower():
                return category

    return "Other"    

def main_menu(transactions, rules, rules_path):
    while True:
        print("\n===== Bill Tracker =====\n")
        print("1. View Transactions")
        print("2. Manage Categories")
        print("3. View Spending Summary")
        print("4. Exit\n")

        choice = input("Select an option: ")

        match choice:
            case "1":
                print("\n===== Transactions =====")
                print(transactions)

            case "2":
                category_menu(rules, rules_path)
                transactions["category"] = transactions["description"].apply(categorize_transaction, args=(rules,))

            case "3":
                print("Feature not implemented yet.")

            case "4":
                break

            case _:
                print("Invalid input. Please select options from 1 to 4.")


def category_menu(rules, rules_path):
    while True:
        print("\n===== Manage Categories =====\n")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Rename Category")
        print("4. Remove Category")
        print("5. Manage Keywords")
        print("6. Back\n")

        choice = input("Select an option: ")

        match choice:
            case "1":
                print("\n===== Existing Categories: =====")
                for category in rules:
                    print(category)

            case "2":
                print("\n===== Existing Categories: =====")
                for category in rules:
                    print(category)

                new_category = input("\nEnter new category name: ").strip()
                while new_category == "":
                    print("Category name cannot be empty. Try again.")
                    new_category = input("Enter new category name: ").strip()

                for category in rules:
                    if new_category.lower() == category.lower():
                        print(f"Category '{new_category}' already exists.")
                        break
                else:
                    rules[new_category] = []
                    save_category_rules(rules_path, rules)
                    print(f"Category '{new_category}' saved successfully.")
        
 
            case "3":
                print("\n===== Existing Categories: =====")
                for category in rules:
                    print(category)

                old_category = input("\nEnter category to rename: ").strip()
                for category in rules:
                    if old_category.lower() == category.lower():
                        old_category = category
                        break
                else:
                    print("Category not found.")
                    continue

                if old_category == "Other":
                    print("The 'Other' category cannot be renamed.")
                    continue
                else:
                    while True:
                        new_category = input("Enter new category name: ").strip()

                        if new_category == "":
                            print("Category name cannot be empty.")
                            continue

                        if new_category == old_category:
                            print(f"Category '{old_category}' already has that name. Try again.")
                            continue

                        for category in rules:
                            if new_category.lower() == category.lower() and category != old_category:
                                print(f"Category '{new_category}' already exists.")
                                break
                        else:
                            rules[new_category] = rules.pop(old_category)
                            save_category_rules(rules_path, rules)
                            print("Category renamed successfully.")
                            break

                        retry = input("Try another name? (y/n): ").strip().lower()
                        if retry != "y":
                            break

            case "4":
                print("\n===== Existing Categories: =====")
                for category in rules:
                    print(category)

                remove_category = input("\nEnter category to remove: ").strip()
                for category in rules:
                    if remove_category.lower() == category.lower():
                        remove_category = category
                        break
                else:
                    print("Category not found.")
                    continue

                if remove_category == "Other":
                    print("The 'Other' category cannot be removed.")
                    continue

                confirmation = input(f"Are you sure you want to remove '{remove_category}'? (y/n): ").strip().lower()
                if confirmation == "y":
                    del rules[remove_category]
                    save_category_rules(rules_path, rules)
                    print(f"Category '{remove_category}' removed successfully.")
                else:
                    print("Category removal cancelled.")

            case "5":
                keyword_menu(rules, rules_path)
            
            case "6":
                break

            case _:
                print("Invalid input. Please select options from 1 to 6.")

def keyword_menu(rules, rules_path):
    while True:
        print("\n===== Manage Keywords =====\n")      
        print("1. View Keywords") 
        print("2. Add Keyword")
        print("3. Remove Keyword")
        print("4. Back\n")

        choice = input("Select an option: ")

        match choice:
            case "1":
                print("\n===== Existing Categories and Keywords: =====")
                for category, keywords in rules.items():
                    print(f"{category}: {', '.join(keywords)}")

            case "2":
                print("\n===== Existing Categories and Keywords: =====")
                for category, keywords in rules.items():
                    print(f"{category}: {', '.join(keywords)}")

                keyword_category = input("\nEnter the category to add a new keyword: ").strip()
                for category in rules:
                    if keyword_category.lower() == category.lower():
                        keyword_category = category
                        break
                else:
                    print("Category not found.")
                    continue

                if keyword_category == "Other":
                    print("'Other' is the default category and cannot have keywords.")
                    continue
                
                new_keyword = input("Enter new keyword: ").strip()

                while new_keyword == "":
                    print("Keyword cannot be empty. Try again.")
                    new_keyword = input("Enter new keyword: ").strip()

                duplicate_found = False
                for category, keywords in rules.items():
                    for keyword in keywords:
                        if new_keyword.lower() == keyword.lower():
                            duplicate_found = True
                            print(f"Keyword '{new_keyword}' already exists.")
                            break
                    if duplicate_found:
                        break

                if not duplicate_found:
                    rules[keyword_category].append(new_keyword)
                    save_category_rules(rules_path, rules)
                    print(f"Keyword '{new_keyword}' saved successfully.")
                          
            case "3":
                print("\n===== Existing Categories and Keywords: =====")
                for category, keywords in rules.items():
                    print(f"{category}: {', '.join(keywords)}")

                keyword_category = input("\nEnter the category to remove a keyword: ").strip()
                for category in rules:
                    if keyword_category.lower() == category.lower():
                        keyword_category = category
                        break
                else:
                    print("Category not found.")
                    continue

                if keyword_category == "Other":
                    print("'Other' is the default category and has no keywords to remove.")
                    continue

                remove_keyword = input("Enter keyword to remove: ").strip()
                for keyword in rules[keyword_category]:
                    if remove_keyword.lower() == keyword.lower():
                        remove_keyword = keyword
                        break
                else:
                    print("Keyword not found.")
                    continue

                confirmation = input(f"Are you sure you want to remove '{remove_keyword}'? (y/n): ").strip().lower()
                if confirmation == "y":
                    rules[keyword_category].remove(remove_keyword)
                    save_category_rules(rules_path, rules)
                    print(f"Keyword '{remove_keyword}' removed successfully.")
                else:
                    print("Keyword removal cancelled.")
    
            case "4":
                break

            case _:
                print("Invalid input. Please select options from 1 to 4.")

>>>>>>> 8923625 (Complete category and keyword management)
def main():
    
    data_path = Path("data") / "sample_transactions.csv"
    transactions = load_transactions(data_path)
    validate_transactions(transactions)
    transactions = clean_transactions(transactions)
<<<<<<< HEAD
=======

    rules_path = Path("config") / "category_rules.json"
    if rules_path.exists():
        rules = load_category_rules(rules_path)
    else:
        rules = {"Shopping": ["amazon", "target"], 
                 "Bills": ["at&t", "comcast", "spotify"],
                 "Other": []}
>>>>>>> 8923625 (Complete category and keyword management)
    
    transactions["category"] = transactions["description"].apply(categorize_transaction, args=(rules,))
    
    main_menu(transactions, rules, rules_path)



if __name__ == "__main__":
    main()


    