import numpy as np
import pandas as pd
from matplotlib import pyplot as plt




def create_aoi_comparison_bar_chart(dataframe, metric_column, group_column):
    aois = dataframe['IA_LABEL'].unique()
    group_labels = dataframe[group_column].unique()
    group_means = {group: [] for group in group_labels}

    for aoi in aois:
        aoi_data = dataframe[dataframe['IA_LABEL'] == aoi]

        for group in group_labels:
            group_data = aoi_data[aoi_data[group_column] == group]
            group_mean = group_data[metric_column].mean()
            group_means[group].append(group_mean)

    x = np.arange(len(aois))  # the label locations
    num_groups = len(group_labels)
    width = 0.8 / num_groups  # the width of the bars

    fig, ax = plt.subplots()

    bars = []
    for i, group in enumerate(group_labels):
        bars.append(ax.bar(x + (i - num_groups/2) * width, group_means[group], width, label=group))

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(metric_column)
    ax.set_title(f'{metric_column} Comparison by AOI')
    ax.set_xticks(x)
    ax.set_xticklabels(aois, rotation=45, ha="right")
    ax.legend()

    fig.tight_layout()

    plt.show()

def top_n_aois(df, column_name, title, n=5):
    # Group by IA_LABEL and calculate the sum of the specified column
    grouped_df = df.groupby('IA_LABEL')[column_name].sum().reset_index()

    # Sort the dataframe by the specified column in descending order
    sorted_df = grouped_df.sort_values(by=column_name, ascending=False)

    # Get the top 5 interest areas
    top_n = sorted_df.head(n)

    # Create a bar chart to visualize the data
    # plt.figure(figsize=(10, 6))
    # plt.bar(top_5['IA_LABEL'], top_5[column_name], color='blue')
    # plt.xlabel('Interest Area')
    # plt.ylabel(column_name)
    # plt.title(title)
    # plt.xticks(rotation=45)
    # plt.tight_layout()

    # Show the bar chart
    # plt.show()

    return top_n


df = pd.read_csv("data/all_participant_clean.csv", delimiter=",")

aggregated_df = df.groupby(['IA_LABEL', 'PARTICIPANT_NUMBER', 'GROUP', 'DEFECTS_FOUND', "IA_AREA"]).agg({
    'IA_RUN_COUNT': 'mean',
    'IA_DWELL_TIME_NORM': 'mean',
    'IA_FIXATION_COUNT': 'mean',
    'IA_FIXATION_%': 'mean'
}).reset_index()

# Assuming 'aggregated_df' is your aggregated dataframe
# aggregated_df['IA_RUN_COUNT'] = aggregated_df['IA_RUN_COUNT'] / aggregated_df['IA_AREA']
aggregated_df['IA_DWELL_TIME_NORM'] = aggregated_df['IA_DWELL_TIME_NORM'] / aggregated_df['IA_AREA']


aggregated_df = aggregated_df[~aggregated_df['IA_LABEL'].str.contains('method_body')]

# Filter dataframes by GROUP
novice_df = aggregated_df[aggregated_df['GROUP'] == 'novice']
expert_df = aggregated_df[aggregated_df['GROUP'] == 'expert']

# Filter dataframes by DEFECTS_FOUND
defects_0_df = aggregated_df[aggregated_df['DEFECTS_FOUND'] == 0]
defects_1_df = aggregated_df[aggregated_df['DEFECTS_FOUND'] == 1]
defects_2_df = aggregated_df[aggregated_df['DEFECTS_FOUND'] == 2]
defects_3_df = aggregated_df[aggregated_df['DEFECTS_FOUND'] == 3]

create_aoi_comparison_bar_chart(aggregated_df, 'IA_DWELL_TIME_NORM', 'DEFECTS_FOUND')
