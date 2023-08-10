import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

participants = pd.read_csv("data/demographics.csv", delimiter=';')

# Calculate the percentages for 'gender' and 'group' columns
gender_percentages = (participants['gender'].value_counts(normalize=True) * 100).round(2)
group_percentages = (participants['group'].value_counts(normalize=True) * 100).round(2)

# Combine 'gender' and 'group' percentages into a single DataFrame
combined_percentages = pd.concat([gender_percentages, group_percentages], axis=1)
combined_percentages.columns = ['Gender', 'Group']

# Create a horizontal bar plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plot the 'Gender' bars
sns.barplot(x=gender_percentages.values, y=gender_percentages.index, color='skyblue', label='Gender', ci=None)

# Plot the 'Group' bars below 'Gender'
sns.barplot(x=group_percentages.values, y=group_percentages.index, color='lightcoral', label='Group', ci=None)

# Set the title and labels
plt.title('Gender and Group Distribution of Participants (100% Stacked)')
plt.xlabel('Percentage')
plt.ylabel('Categories')

# Display the percentages within each bar
for i, v in enumerate(gender_percentages.values):
    plt.text(v / 2, i, f'{v:.2f}%', ha='center', va='center', fontweight='bold')

for i, v in enumerate(group_percentages.values):
    plt.text(gender_percentages.values[-1] + v / 2, i, f'{v:.2f}%', ha='center', va='center', fontweight='bold')

# Show the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()