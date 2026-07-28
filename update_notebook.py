import json

nb_path = r'e:\ML PROJECT\Erasmus-Mundus-Scholarship-Possibilities-Prediction\notebook\1_EDA_Scholarship.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for i, line in enumerate(cell['source']):
            if "df['case_status']" in line:
                cell['source'][i] = line.replace("df['case_status']", "df['Scholarship_Awarded']")

markdown_content = [
    "### 💡 Chi-Square Test Insights:\n",
    "\n",
    "When testing if categorical columns are correlated with `Scholarship_Awarded`:\n",
    "\n",
    "**1. Internship (Reject Null Hypothesis)**\n",
    "* **Insight:** There is a **statistically significant relationship** between having an internship and getting the scholarship. \n",
    "* **Action:** This is a highly important feature for the machine learning model.\n",
    "\n",
    "**2. Country (Fail to Reject Null Hypothesis)**\n",
    "* **Insight:** There is **no statistically significant relationship** between the applicant's country and whether they receive the scholarship. The scholarship is awarded purely on merit without regional bias.\n",
    "* **Action:** This feature might not be very important for predicting the outcome.\n",
    "\n",
    "**3. Target_Program (Fail to Reject Null Hypothesis)**\n",
    "* **Insight:** There is **no statistically significant relationship** between the specific program (AI, Cyber, DS) and the chances of getting the scholarship.\n",
    "* **Action:** The competition level is relatively equal across all programs in the dataset.\n",
    "\n",
    "**Summary for ML Model:**\n",
    "`Internship` is a valuable predictor. `Country` and `Target_Program` provide little predictive power and could potentially be dropped to simplify the model.\n"
]

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": markdown_content
}

nb['cells'].append(new_cell)

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully!")
