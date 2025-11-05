import pandas as pd 

def total_loans(df:pd.DataFrame) -> int:
    return df["loan_id"].nunique()

def avg_loan_days(df:pd.DataFrame) -> float:
    return float(df["loan_day"].mean())

def overdue_rate(df:pd.DataFrame) -> float :
    return float((df["overdue_days"] > 0).mean())

