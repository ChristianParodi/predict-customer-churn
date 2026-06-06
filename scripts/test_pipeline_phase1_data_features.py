import os
import pandas as pd
import sys
sys.path.append(os.path.abspath("src"))

# modules
from data.load_data import load_data
from data.preprocess import preprocess_data
from features.build_features import build_features

DATA_PATH = "data/raw/churn_data.csv"
TARGET_COL = "Churn"

def main():
  print(f"Testing phase 1: load -> preprocess -> build features")

  df = load_data(DATA_PATH)
  print("1. Data loaded.")

  df_clean = preprocess_data(df, target_col=TARGET_COL)
  print("2. Data preprocessed.")

  df_features = build_features(df_clean, target_col=TARGET_COL)
  print("3. Features built.")

if __name__ == "__main__":
  main()

