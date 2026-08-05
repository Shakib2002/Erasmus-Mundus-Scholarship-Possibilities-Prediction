import json

filepath = 'e:/ML PROJECT/Erasmus-Mundus-Scholarship-Possibilities-Prediction/notebook/2_Feature_Engineering_and_Model_Training.ipynb'
with open(filepath, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if "best_model = KNeighborsClassifier(**model_param['KNN'])" in source:
            cell['source'] = [
                "best_model_name = tuned_report.iloc[0]['Model Name']\n",
                "best_model = best_models[best_model_name]\n",
                "best_model = best_model.fit(X_train_res, y_train_res)\n",
                "y_pred = best_model.predict(X_test)\n",
                "score = accuracy_score(y_test,y_pred)\n",
                "cr = classification_report(y_test,y_pred)\n",
                "\n",
                "print(f\"FINAL MODEL '{best_model_name}'\")\n",
                "print(\"Accuracy Score value: {:.4f}\".format(score))\n",
                "print(cr)\n"
            ]
    elif cell['cell_type'] == 'markdown':
        source = ''.join(cell['source'])
        if "Best Model is K-Nearest Neighbor(KNN)" in source or "Best Model is K-Nearest" in source:
            cell['source'] = [
                "## Final Model Evaluation\n",
                "*(The best model is now chosen automatically based on the tuned_report dataframe above)*"
            ]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
