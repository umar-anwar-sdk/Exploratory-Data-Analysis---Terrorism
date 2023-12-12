# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset with dtype specification and low_memory=False
dtype_specification = {'latitude': 'float64', 'longitude': 'float64', 'success': 'int64', 'suicide': 'int64', 'nkill': 'float64', 'nwound': 'float64'}
df = pd.read_csv("globalterrorismdb_0718dist.csv", encoding="latin-1", dtype=dtype_specification, low_memory=False)

# Select relevant columns for analysis
cols_to_keep = ['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate', 'city', 'success', 'suicide', 'attacktype1_txt', 'targtype1_txt', 'weaptype1_txt', 'nkill', 'nwound']
df = df[cols_to_keep]

# Handle missing values
df.dropna(inplace=True)

# Get the top 10 countries based on the number of attacks
top_countries = df['country_txt'].value_counts().nlargest(10).index
df_top_countries = df[df['country_txt'].isin(top_countries)]

# Set the style of seaborn
sns.set(style="whitegrid")

# Bar Plot for Top 10 Countries
plt.figure(figsize=(14, 8))

# Example: Barplot of 'country_txt' with 'attacktype1_txt' as hue
plot = sns.countplot(y='country_txt', hue='attacktype1_txt', data=df_top_countries, palette='viridis')
plot.set(title='Distribution of Attack Types in Top 10 Countries', xlabel='Number of Attacks', ylabel='Country')
plot.legend(title='Attack Type', loc='upper right')

plt.show()
