import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/type-chart.py')

df['Defense'] = df['defense-type1'] + " / " + df['defense-type2']

df.set_index('Defense', inplace=True)
df.drop(columns=['defense-type1', 'defense-type2'], inplace=True)

plt.figure(figsize=(16, 10))
sns.heatmap(df, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Pokémon Type Effectiveness Heatmap")
plt.xlabel("Attack Types")
plt.ylabel("Defense Combinations")
plt.xticks(rotation=45)
plt.show()
plt.savefig('imgs/heatmap_tipos.png')