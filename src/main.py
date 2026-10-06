import pandas as pd
from pathlib import Path

def load_transactions(file_path):
    return pd.read_csv(file_path)
                    
def main():
    
    file_path = Path("data") / "sample_transactions.csv"
    transactions = load_transactions(file_path)
    
    print("Bill Tracker started")
    print(transactions)


if __name__ == "__main__":
    main()
    