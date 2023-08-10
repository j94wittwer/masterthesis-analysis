import pandas as pd
from scipy.stats import chi2_contingency
from statsmodels.sandbox.stats.multicomp import multipletests
import tabulate as tbl

data = pd.read_csv("data/novice_expert_defect_comparison.csv", delimiter=";")

print(data.head())

defects = ["PARAM_ORDER_FOUND", "LACK_PERS_FOUND", "FLAW_LOGIC_FOUND"]

p_values = []

for defect in defects:
    contingency_table = pd.crosstab(data["GROUP"], data[defect])

    chi2, p, dof, expected = chi2_contingency(contingency_table)

    p_values.append(p)

    print(f"Defect: {defect}")
    print(f"Chi-squared value: {chi2}")
    print(f"P-value: {p}")
    print(f"Degrees of freedom: {dof}")
    print("----")

# Apply Holm-Bonferroni correction
reject, adjusted_p_values, _, _ = multipletests(p_values, method='holm')

# Print the adjusted p-values
for i, defect in enumerate(defects):
    print(f"Adjusted p-value for {defect}: {adjusted_p_values[i]}")
    print("Null Hypothesis will be rejected") if reject[i] else print("Null Hypothesis will not be rejected")

table_data = []
for i, defect in enumerate(defects):
    table_data.append([defect, p_values[i], adjusted_p_values[i], reject[i]])

# Define table headers
headers = ['Defect', 'Unadjusted p-value', 'Adjusted p-value', 'Significant']

# Create the table
result_table = tbl.tabulate(table_data, headers=headers, tablefmt='grid')

# Print or save the table
print(result_table)
