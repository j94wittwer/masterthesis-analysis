import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from util import mann_whitney_u_test
from scipy.stats import kruskal

data = {
    'PARTICIPANT': [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14],
    'GROUP': ['novice', 'expert', 'expert', 'novice', 'novice', 'novice', 'expert', 'expert', 'novice', 'expert',
              'novice', 'expert', 'novice'],
    'AVERAGE_DIRECTION': [15, 3, 13, 3, 5, 0, 16, 65, 10, 10, 10, 3, 9],
    'REGRESSION_RATE': [47.95, 48.72, 46.7, 20.0, 49.11, 50.0, 47.99, 45.97, 49.2, 48.87, 49.2, 49.53, 47.27],
    'DEFECTS_FOUND': [1, 2, 1, 1, 0, 1, 1, 3, 2, 3, 0, 2, 0]
}

df = pd.DataFrame(data)

# Create a boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='GROUP', y='REGRESSION_RATE', data=df, showfliers=False)
plt.title('Regression Rate by Group')
plt.ylabel('Regression Rate')
plt.show()

# Calculate descriptive statistics for each group
group_statistics = df.groupby('GROUP')['REGRESSION_RATE'].agg(['mean', 'std'])

print(group_statistics)

experts_df = df[df['GROUP'] == 'expert']
novices_df = df[df['GROUP'] == 'novice']

no_defect_df = df[df['DEFECTS_FOUND'] == 0]['REGRESSION_RATE']
one_defect_df = df[df['DEFECTS_FOUND'] == 1]['REGRESSION_RATE']
two_defect_df = df[df['DEFECTS_FOUND'] == 2]['REGRESSION_RATE']
three_defect_df = df[df['DEFECTS_FOUND'] == 3]['REGRESSION_RATE']

mann_whitney_u_test(experts_df['REGRESSION_RATE'], novices_df['REGRESSION_RATE'], 'REGRESSION_RATE',
                    tablefmt='fancy_grid')

groups = [no_defect_df, one_defect_df, two_defect_df, three_defect_df]

statistic, p_value = kruskal(*groups)

# Print the results
print("Kruskal-Wallis statistic:", statistic)
print("p-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There are significant differences between groups.")
else:
    print("Fail to reject the null hypothesis: No significant differences between groups.")

# Calculate mean and std for each dataframe
means = [no_defect_df.mean(),
         one_defect_df.mean(),
         two_defect_df.mean(),
         three_defect_df.mean()]

stds = [no_defect_df.std(),
        one_defect_df.std(),
        two_defect_df.std(),
        three_defect_df.std()]

# Create a new dataframe
summary_df = pd.DataFrame({'mean': means, 'std': stds},
                          index=['No Defect', 'One Defect', 'Two Defects', 'Three Defects'])

print(summary_df)
