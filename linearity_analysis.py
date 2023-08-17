import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import control_flow_path
import scan_path

ideal_sequence = scan_path.optimal_run
participants_sequences = control_flow_path.all_participants

aois = pd.read_csv("data/aois.csv", delimiter=";")

aoi_dict = {}

for aoi_id, position in enumerate(ideal_sequence):
    aoi_info = aois[aois['ID'] == position].iloc[0]
    aoi_attributes = {
        'label': aoi_info['LABEL'],
        'class': aoi_info['CLASS'],
        'type': aoi_info['TYPE'],
        'position': aoi_id
    }
    aoi_dict[position] = aoi_attributes

class_transitions = np.zeros((4, 4), dtype=int)

class_transition_matrices = {}

# Analyze each participant's sequence
for participant, sequence in participants_sequences.items():

    print(participant)

    # Calculate average direction
    average_direction = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            average_direction += 1
        elif sequence[i] > sequence[i + 1]:
            average_direction -= 1
    # average_direction /= len(sequence) - 1  # Normalize

    # Calculate class transitions
    for i in range(len(sequence) - 1):
        start_class = aoi_dict[sequence[i]]['class']
        target_class = aoi_dict[sequence[i + 1]]['class']
        start_index = ['CONTROLLER', 'SERVICE', 'USER', 'REPOSITORY'].index(start_class)
        target_index = ['CONTROLLER', 'SERVICE', 'USER', 'REPOSITORY'].index(target_class)
        class_transitions[start_index, target_index] += 1

    # Calculate regression rate
    backward_transitions = sum(1 for i in range(len(sequence) - 1) if sequence[i] > sequence[i + 1])
    regression_rate = backward_transitions / (len(sequence) - 1) * 100

    class_transitions_relative = np.zeros((4, 4), dtype=float)

    total_transitions = sum(sum(class_transitions))

    for row in range(4):
        for col in range(4):
            value = class_transitions[row, col]
            class_transitions_relative[row, col] = round((value / total_transitions) * 100, 3)

    class_transitions_df = pd.DataFrame(class_transitions, columns=['CONTROLLER', 'SERVICE', 'USER', 'REPOSITORY'],
                                        index=['CONTROLLER', 'SERVICE', 'USER', 'REPOSITORY'])

    class_transitions_relative_df = pd.DataFrame(class_transitions_relative,
                                                 columns=['CONTROLLER', 'SERVICE', 'USER', 'REPOSITORY'],
                                                 index=['CONTROLLER', 'SERVICE', 'USER', 'REPOSITORY'])

    class_transition_matrices[participant] = class_transitions_relative_df

    # Print results for the participant
    print(f"Participant: {participant}")
    print(f"Average Direction: {average_direction}")
    print("Class Transitions Matrix:")
    print(class_transitions_df)
    print("")
    print("Percentages of Transitions:")
    print(class_transitions_relative_df)
    print(f"Regression Rate: {regression_rate:.2f}%")
    print("=" * 40)

fig_heatmap, axes_heatmap = plt.subplots(4, 4, figsize=(15, 15), gridspec_kw={'wspace': 0.6, 'hspace': 0.6})
fig_heatmap.suptitle('Transition Matrix Heatmaps')

fig_clustermap, axes_clustermap = plt.subplots(1, len(class_transition_matrices), figsize=(15, 5))
fig_clustermap.suptitle('Transition Matrix Clustermaps')

for i, (participant, matrix_df) in enumerate(class_transition_matrices.items()):
    row = i // 4
    col = i % 4

    # Heatmap
    sns.heatmap(matrix_df, annot=True, fmt=".3g", cmap="YlGnBu", ax=axes_heatmap[row, col])
    axes_heatmap[row, col].set_title(f'{participant}')
    axes_heatmap[row, col].set_xticklabels(axes_heatmap[row, col].get_xticklabels(), rotation=45, ha="right")

    # Clustermap
    # sns.clustermap(matrix_df, annot=True, fmt=".3g", cmap="YlGnBu", ax=axes_clustermap[i])
    # axes_clustermap[i].set_title(f'Participant {participant}')

plt.tight_layout()
plt.show()

data = {
    'GROUP': ['novice', 'expert', 'expert', 'novice', 'novice', 'novice', 'expert', 'expert', 'novice', 'expert',
              'novice', 'expert', 'novice'],
    'AVERAGE_DIRECTION': [15, 3, 13, 3, 5, 0, 16, 65, 10, 10, 10, 3, 9],
    'REGRESSION_RATE': [47.95, 48.72, 46.7, 20.0, 49.11, 50.0, 47.99, 45.97, 49.2, 48.87, 49.2, 49.53, 47.27]
}

