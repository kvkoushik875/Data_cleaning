import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

# CELL 2: Load dataset and initial inspection
try:
    df = pd.read_csv(r"D:\Digital Twin based EV charging station navigations\global_ev_charging_station.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("File not found.")
    df = None

if df is not None:
    print("--- Initial Data Info ---")

    # Drop UUID if you don't need it for analysis
    if 'UUID' in df.columns:
        df.drop(columns=['UUID'], inplace=True)
        print("Dropped 'UUID' column as it is mostly an identifier.")

    df.info()

    print("\n--- First 5 Rows ---")
    print(df.head())
    print(f"\nInitial dataset shape: {df.shape}")

print(f"Original shape: {df.shape}")
print(f"Original columns: {list(df.columns)}")

columns_to_keep = [
    "StationID",
    "Operator",
    "UsageType",
    "AddressTitle",
    "Town",
    "StateOrProvince",
    "Country",
    "Latitude",
    "Longitude",
    "MaxPowerKW",
    "FastChargeCount",
    "ConnectionTypes",
    "StatusType"
]

columns_removed = [col for col in df.columns if col not in columns_to_keep]
print(f"\nColumns removed: {columns_removed}")


df_filtered = df[columns_to_keep]

print(f"\nFiltered shape: {df_filtered.shape}")
print(f"Remaining columns: {list(df_filtered.columns)}")

df_filtered.to_csv("global_ev_charging_station_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as 'global_ev_charging_station_cleaned.csv'")

