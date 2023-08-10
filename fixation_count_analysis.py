import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from util import test_normal_distribution, mann_whitney_u_test

df = pd.read_csv("data/all_participant_clean.csv", delimiter=",")

# Get dataframes grouped by group
experts_df = df[df['GROUP'] == 'expert']
novices_df = df[df['GROUP'] == 'novice']

fixation_count_norm = 'IA_FIXATION_COUNT_NORM'

experts_fixation_norm_mean = experts_df[fixation_count_norm].mean()
novices_fixation_norm_mean = novices_df[fixation_count_norm].mean()

experts_fixation_norm_std = experts_df[fixation_count_norm].std()
novices_fixation_norm_std = novices_df[fixation_count_norm].std()


plt.figure(figsize=(8,6))
sns.boxplot(x='GROUP', y=fixation_count_norm, data=df)
plt.ylabel('Normalized Fixation Count')
plt.show()


mann_whitney_u_test(novices_df[fixation_count_norm], experts_df[fixation_count_norm], fixation_count_norm, tablefmt='fancy_grid')

print(f"Expert mean: {round(experts_fixation_norm_mean, 3)}")
print(f"Expert std: {round(experts_fixation_norm_std, 3)}")
print(f"Novice mean: {round(novices_fixation_norm_mean, 3)}")
print(f"Novice std: {round(novices_fixation_norm_std, 3)}")
