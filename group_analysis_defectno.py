import math

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tabulate

from scipy.stats import kruskal
import scikit_posthocs as sp

from util import test_normal_distribution, mann_whitney_u_test

df = pd.read_csv("data/all_participants.csv", delimiter=";")

# Replace value with variable that should be tested
test_variable = 'IA_FIRST_RUN_TOTAL_TIME'

for index, row in df.iterrows():
    value = row[test_variable]
    if value == '.' or value == '#WERT!' or math.isnan(value):
        df.at[index, test_variable] = 0
    else:
        df.at[index, test_variable] = int(value)

# Get dataframes grouped by group
no_defect_df = df[df['DEFECTS_FOUND'] == 0]
one_defect_df = df[df['DEFECTS_FOUND'] == 1]
two_defect_df = df[df['DEFECTS_FOUND'] == 2]
three_defect_df = df[df['DEFECTS_FOUND'] == 3]

# Calculate mean and std for each dataframe
means = [no_defect_df[test_variable].mean(),
         one_defect_df[test_variable].mean(),
         two_defect_df[test_variable].mean(),
         three_defect_df[test_variable].mean()]

stds = [no_defect_df[test_variable].std(),
        one_defect_df[test_variable].std(),
        two_defect_df[test_variable].std(),
        three_defect_df[test_variable].std()]

# Create a new dataframe
summary_df = pd.DataFrame({'mean': means, 'std': stds},
                          index=['No Defect', 'One Defect', 'Two Defects', 'Three Defects'])

# Group the data by the "DEFECTS_FOUND" column and collect "IA_DWELL_TIME_NORM" values
groups = []
for i in range(4):  # Considering the values are 0, 1, 2, 3
    group_data = df[df['DEFECTS_FOUND'] == i][test_variable]
    groups.append(group_data)

# Perform the Kruskal-Wallis test
statistic, p_value = kruskal(*groups)

print(tabulate.tabulate(summary_df, tablefmt='latex', headers='keys'))

# Print the results
print("Kruskal-Wallis statistic:", statistic)
print("p-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There are significant differences between groups.")
else:
    print("Fail to reject the null hypothesis: No significant differences between groups.")

results = sp.posthoc_dunn(groups, p_adjust='holm')
print(results)

print(tabulate.tabulate(results, tablefmt='latex', headers='keys'))
