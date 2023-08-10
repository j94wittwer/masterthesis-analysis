import re

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from util import test_normal_distribution, mann_whitney_u_test

df = pd.read_csv("data/all_participants.csv", delimiter=";")

first_run_total_time = 'IA_FIRST_RUN_TOTAL_TIME'

for index, row in df.iterrows():
    value = row[first_run_total_time]
    if value == '.':
        df.at[index, first_run_total_time] = 0
    else:
        df.at[index, first_run_total_time] = int(value)

experts_df = df[df['GROUP'] == 'expert']
novices_df = df[df['GROUP'] == 'novice']

experts_mean = experts_df[first_run_total_time].mean()
experts_std = experts_df[first_run_total_time].std()

novices_mean = novices_df[first_run_total_time].mean()
novices_std = novices_df[first_run_total_time].std()


plt.figure(figsize=(8,6))
sns.boxplot(x='GROUP', y=first_run_total_time, data=df)
plt.ylabel('First Run Total Time')
plt.show()

mann_whitney_u_test(novices_df[first_run_total_time], experts_df[first_run_total_time], first_run_total_time, tablefmt='fancy_grid')

print(f"Expert mean: {round(experts_mean, 3)}")
print(f"Expert std: {round(experts_std, 3)}")
print(f"Novice mean: {round(novices_mean, 3)}")
print(f"Novice std: {round(novices_std, 3)}")
