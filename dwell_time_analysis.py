import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from util import test_normal_distribution, mann_whitney_u_test

df = pd.read_csv("data/all_participant_clean.csv", delimiter=",")

# Get dataframes grouped by group
experts_df = df[df['GROUP'] == 'expert']
novices_df = df[df['GROUP'] == 'novice']

dwell_time = 'IA_DWELL_TIME_NORM'

print(experts_df.head())

# Get mean and std for experts
expert_dwell_mean = experts_df[dwell_time].mean()
expert_dwell_std = experts_df[dwell_time].std()

# Get mean and std for novices
novice_dwell_mean = novices_df[dwell_time].mean()
novice_dwell_std = novices_df[dwell_time].std()

plt.figure(figsize=(8, 6))
sns.boxplot(x='GROUP', y=dwell_time, data=df)
plt.ylabel('Normalized Dwell Time')
plt.show()

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
sns.histplot(experts_df[dwell_time], kde=True, label='Experts')
sns.histplot(novices_df[dwell_time], kde=True, label='Novices')
plt.xlabel('Normalized Dwell Time on AOIs')
plt.ylabel('Frequency')
plt.legend()
plt.show()

test_normal_distribution(novices_df[dwell_time])
test_normal_distribution(experts_df[dwell_time])

mann_whitney_u_test(novices_df[dwell_time], experts_df[dwell_time], dwell_time, tablefmt='latex')

print(f"Expert mean: {round(expert_dwell_mean, 3)}")
print(f"Expert std: {round(expert_dwell_std, 3)}")
print(f"Novice mean: {round(novice_dwell_mean, 3)}")
print(f"Novice std: {round(novice_dwell_std, 3)}")
