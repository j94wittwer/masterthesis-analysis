import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from util import mann_whitney_u_test

data = {
    'GROUP': ['novice', 'expert', 'expert', 'novice', 'novice', 'novice', 'expert', 'expert', 'novice', 'expert',
              'novice', 'expert', 'novice'],
    'AVERAGE_DIRECTION': [15, 3, 13, 3, 5, 0, 16, 65, 10, 10, 10, 3, 9],
    'REGRESSION_RATE': [47.95, 48.72, 46.7, 20.0, 49.11, 50.0, 47.99, 45.97, 49.2, 48.87, 49.2, 49.53, 47.27]
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

mann_whitney_u_test(experts_df['REGRESSION_RATE'], novices_df['REGRESSION_RATE'], 'REGRESSION_RATE', tablefmt='fancy_grid')
