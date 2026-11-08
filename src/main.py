from pathlib import Path
import pandas as pd

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
                    
def main():
    
    file_path = Path("data") / "sample_transactions.csv"
    transactions = load_transactions(file_path)
    validate_transactions(transactions)
    transactions = clean_transactions(transactions)
    
    print("Bill Tracker started")
    print(transactions)


if __name__ == "__main__":
    main()


    