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
                    
def main():
    
    file_path = Path("data") / "sample_transactions.csv"
    transactions = load_transactions(file_path)
    validate_transactions(transactions)
    
    print("Bill Tracker started")
    print(transactions)

if __name__ == "__main__":
    main()


    