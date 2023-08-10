import pandas as pd
import numpy as np

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


class_transitions = np.zeros((4,4), dtype=int)

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
    average_direction /= len(sequence) - 1  # Normalize

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

    # Print results for the participant
    print(f"Participant: {participant}")
    print(f"Average Direction: {average_direction}")
    print("Class Transitions Matrix:")
    print(class_transitions)
    print(f"Regression Rate: {regression_rate:.2f}%")
    print("=" * 40)

