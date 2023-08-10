import pandas as pd

# Replace 'your_data.csv' with your actual data file
df = pd.read_csv('data/all_participants_raw.csv', delimiter=";")

# Step 1: Remove the 'IA_DWELL_TIME_NORM' column if it exists
if 'IA_DWELL_TIME_NORM' in df.columns:
    df.drop(columns=['IA_DWELL_TIME_NORM'], inplace=True)

if 'IA_FIXATION_COUNT_NORM' in df.columns:
    df.drop(columns=['IA_FIXATION_COUNT_NORM'], inplace=True)

# Step 2 and 3: Calculate normalized Dwell Time for each row
normalized_dwell_time = []
normalized_fixation_count = []

for index, row in df.iterrows():
    participant_number = row['PARTICIPANT_NUMBER']
    min_dwell_time = df[df['PARTICIPANT_NUMBER'] == participant_number]['IA_DWELL_TIME'].min()
    max_dwell_time = df[df['PARTICIPANT_NUMBER'] == participant_number]['IA_DWELL_TIME'].max()

    if max_dwell_time - min_dwell_time != 0:
        norm_value = (row['IA_DWELL_TIME'] - min_dwell_time) / (max_dwell_time - min_dwell_time)
    else:
        norm_value = 0  # Avoid division by zero

    normalized_dwell_time.append(norm_value)

    min_fixation_count = df[df['PARTICIPANT_NUMBER'] == participant_number]['IA_FIXATION_COUNT'].min()
    max_fixation_count = df[df['PARTICIPANT_NUMBER'] == participant_number]['IA_FIXATION_COUNT'].max()

    if max_fixation_count - min_fixation_count != 0:
        norm_value = (row['IA_FIXATION_COUNT'] - min_fixation_count) / (max_fixation_count - min_fixation_count)
    else:
        norm_value = 0

    normalized_fixation_count.append(norm_value)


# Add the normalized values to the DataFrame
df['IA_DWELL_TIME_NORM'] = normalized_dwell_time
df['IA_FIXATION_COUNT_NORM'] = normalized_fixation_count

# Save the updated DataFrame to a new CSV file
df.to_csv('data/all_participant_clean.csv', index=False)
