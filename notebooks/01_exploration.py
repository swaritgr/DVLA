import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better plots
sns.set(style="whitegrid")

# =====================
# Load the data
# =====================
# ⚠️ Update this path if using Google Drive or local
file_path = '/content/drive/MyDrive/DVLA_data/df_VEH0160_GB.csv'

# Load CSV
try:
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully.")
except Exception as e:
    print(f"❌ Error loading data: {e}")

# =====================
# Filter EV data
# =====================
df_ev = df[df['Fuel'] == 'Electric']
print(f"Total EV records: {df_ev.shape[0]}")

# =====================
# Explore top makes and models
# =====================
top_makes = df_ev['Make'].value_counts().head(10)
print("Top EV makes:")
print(top_makes)

# =====================
# Prepare trend data
# =====================
# Get quarterly columns
quarter_cols = [col for col in df_ev.columns if 'Q' in col]

# Melt dataframe for time series plot
df_ev_melted = df_ev.melt(id_vars=['Make', 'Model'], value_vars=quarter_cols, 
                          var_name='Quarter', value_name='Count')

# Group by quarter to get total EV count
df_ev_trend = df_ev_melted.groupby('Quarter')['Count'].sum().reset_index()

# Sort quarters correctly
df_ev_trend = df_ev_trend.sort_values('Quarter')

# =====================
# Plot EV trend
# =====================
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_ev_trend, x='Quarter', y='Count', marker="o")
plt.title('EV stock trend over time (Great Britain)')
plt.xlabel('Quarter')
plt.ylabel('Number of EVs')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# =====================
# Save processed EV data (optional)
# =====================
# df_ev.to_csv('/content/drive/MyDrive/DVLA_data/processed/df_EV_processed.csv', index=False)
# print("✅ Processed EV data saved.")

print("🎉 Exploration complete!")
