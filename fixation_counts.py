import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ia_fixation_count_group.csv", delimiter=";")

# Create the violin plot using Seaborn
plt.figure(figsize=(10, 6))
sns.violinplot(x='IA_LABEL', y='IA_FIXATION_COUNT', hue='GROUP', data=df, split=True, inner='quart', palette='muted')
plt.xlabel('IA_LABEL')
plt.ylabel('IA_FIXATION_COUNT')
plt.title('Violin Plot of IA_FIXATION_COUNT for each IA_LABEL')

# Show the plot
plt.tight_layout()
plt.show()