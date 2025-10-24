import pandas as pd
import os
print("Current working directory:", os.getcwd())

# Load both CSVs
losses = pd.read_csv("data/NBATrackingDataLosses24-25.csv")
wins = pd.read_csv("data/NBATrackingDataWins24-25.csv")

# Find shared players (intersection)
shared_players = set(losses["PLAYER"]) & set(wins["PLAYER"])

# Keep only rows with shared players
losses_clean = losses[losses["PLAYER"].isin(shared_players)]
wins_clean = wins[wins["PLAYER"].isin(shared_players)]

# Save cleaned versions
losses_clean.to_csv("data/NBATrackingDataLosses24-25_clean.csv", index=False)
wins_clean.to_csv("data/NBATrackingDataWins24-25_clean.csv", index=False)

print(f"Cleaned datasets saved! Each now has {len(shared_players)} players.")