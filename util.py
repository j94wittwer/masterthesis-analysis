import pandas as pd
from scipy.stats import shapiro, mannwhitneyu
from tabulate import tabulate
from pingouin import mwu

all_participants = {
    1: {
        'group': 'novice',
        'defects_found': 1
    },
    2: {
        'group': 'expert',
        'defects_found': 2
    },
    3: {
        'group': 'expert',
        'defects_found': 1
    },
    4: {
        'group': 'novice',
        'defects_found': 1
    },
    5: {
        'group': 'novice',
        'defects_found': 0
    },
    6: {
        'group': 'novice',
        'defects_found': 1
    },
    7: {
        'group': 'expert',
        'defects_found': 1
    },
    8: {
        'group': 'expert',
        'defects_found': 3
    },
    9: {
        'group': 'novice',
        'defects_found': 2
    },
    11: {
        'group': 'expert',
        'defects_found': 2
    },
    12: {
        'group': 'novice',
        'defects_found': 0
    },
    13: {
        'group': 'expert',
        'defects_found': 2
    },
    14: {
        'group': 'novice',
        'defects_found': 0
    },
}


def test_normal_distribution(data, alpha=0.05):
    statistic, p_value = shapiro(data)

    print(f"Shapiro-Wilk Test:")
    print(f"Test statistic: {statistic}")
    print(f"P-Value: {p_value}")

    if p_value > alpha:
        print("The data is normally distributed (fail to reject H0)")
    else:
        print("The data is not normally distributed (reject H0)")


def calculate_effect_size(group1, group2):
    diff_mean = group1.mean() - group2.mean()
    pooled_std = ((group1.var() + group2.var()) / 2) ** 0.5
    effect_size = diff_mean / pooled_std
    return effect_size


def calculate_z_score(group1, group2):
    diff_mean = group1.mean() - group2.mean()
    pooled_std = ((group1.var() + group2.var()) / 2) ** 0.5
    z_score = diff_mean / pooled_std
    return z_score


def mann_whitney_u_test(group1, group2, index, alpha=0.05, tablefmt='fancy_grid'):
    statistic, p_value = mannwhitneyu(group1, group2)

    if p_value < alpha:
        result = "Significant"
    else:
        result = "Not Significant"

    effect_size = calculate_effect_size(group1, group2)
    z_score = calculate_z_score(group1, group2)

    table = pd.DataFrame({
        'Group 1 Median': [round(group1.median(), 3)],
        'Group 1 n': [len(group1)],
        'Group 2 Median': [round(group2.median(), 3)],
        'Group 2 n': [len(group2)],
        'Mann-Whitney U': [statistic],
        'p-value': [p_value],
        'Effect Size (Cohen\'s d)': [effect_size],
        'Result': [result]
    }, index=[index])

    table_str = tabulate(table.T, headers='keys', tablefmt=tablefmt)

    print(mwu(group1, group2, alternative='greater'))

    print(table_str)
