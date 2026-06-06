import pandas as pd


def preprocess_data(df: pd.DataFrame, target_col: str = "Churn") -> pd.DataFrame:
    """
    Basic cleaning for Telco churn.
    - trim and rename columns in PascalCase
    - drop ID col
    - fix TotalCharges to numeric
    - map target Churn to 0/1 if needed
    - simple NA handling
    """
    # tidy headers
    df.rename(columns=lambda x: (x[0].upper() + x[1:]).strip(), inplace=True)

    df.drop('CustomerID', axis=1, inplace=True)

    # 0/1 if Yes/No
    if target_col in df.columns and df[target_col].dtype == "object":
        df[target_col] = df[target_col].str.strip().map({"No": 0, "Yes": 1})

    # TotalCharges -> coerce to float
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # SeniorCitizen should be 0/1 ints if present
    if "SeniorCitizen" in df.columns:
        df["SeniorCitizen"] = df["SeniorCitizen"].fillna(0).astype(int)

    # NA strategy:
    # - numeric: fill with 0
    # - others: leave for encoders to handle (get_dummies ignores NaN safely)
    num_cols = df.select_dtypes(include=["number"]).columns
    df[num_cols] = df[num_cols].fillna(0)

    return df
