import os
import pandas as pd

if os.path.exists("new_data.csv"):
    print("🔁 Retraining model with new data...")
else:
    print("No new data found")