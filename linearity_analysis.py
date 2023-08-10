import pandas as pd

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

# Print the resulting dictionary
for aoi_id, attributes in aoi_dict.items():
    print(f"AOI {aoi_id} Attributes: {attributes}")
