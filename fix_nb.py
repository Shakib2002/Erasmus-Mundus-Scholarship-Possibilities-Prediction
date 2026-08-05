import json

filepath = 'e:/ML PROJECT/Erasmus-Mundus-Scholarship-Possibilities-Prediction/notebook/2_Feature_Engineering_and_Model_Training.ipynb'
with open(filepath, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    source = ''.join(cell['source'])
    
    # 1. Fixing the SMOTE & train_test_split cells
    if 'smt.fit_resample(X, y)' in source:
        cell['source'] = [
            "from sklearn.model_selection import train_test_split\n",
            "from imblearn.combine import SMOTETomek, SMOTEENN\n",
            "\n",
            "# 1. SPLIT FIRST\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "\n",
            "# 2. RESAMPLE ONLY THE TRAINING DATA\n",
            "smt = SMOTEENN(random_state=42, sampling_strategy='minority')\n",
            "X_train_res, y_train_res = smt.fit_resample(X_train, y_train)\n"
        ]
        
    if 'train_test_split(X_res,y_res,test_size=0.2,random_state=42)' in source:
        cell['source'] = [
            "# Data is already split and resampled above.\n",
            "print(f\"Resampled Training Set: {X_train_res.shape}\")\n",
            "print(f\"Test Set: {X_test.shape}\")\n"
        ]
        
    # 2. evaluate_models function definition
    if 'def evaluate_models(X, y, models):' in source:
        new_source = []
        for line in cell['source']:
            if 'def evaluate_models(X, y, models):' in line:
                new_source.append('def evaluate_models(X_train, X_test, y_train, y_test, models):\n')
            elif 'X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)' in line:
                pass # skip
            else:
                new_source.append(line)
        cell['source'] = new_source
        
    # 3. base_model_report evaluation
    if 'base_model_report =evaluate_models(X=X_res, y=y_res, models=models)' in source:
        cell['source'] = ["base_model_report = evaluate_models(X_train_res, X_test, y_train_res, y_test, models=models)\n"]
        
    # 4. RandomizedSearchCV loop
    if 'random.fit(X_res, y_res)' in source:
        new_source = []
        for line in cell['source']:
            if 'random.fit(X_res, y_res)' in line:
                new_source.append('    random.fit(X_train_res, y_train_res)\n')
            else:
                new_source.append(line)
        cell['source'] = new_source
        
    # 5. tuned_report evaluation
    if 'tuned_report =evaluate_models(X=X_res, y=y_res, models=best_models)' in source:
        new_source = []
        for line in cell['source']:
            if 'tuned_report =evaluate_models(X=X_res, y=y_res, models=best_models)' in line:
                new_source.append('tuned_report = evaluate_models(X_train_res, X_test, y_train_res, y_test, models=best_models)\n')
            else:
                new_source.append(line)
        cell['source'] = new_source

    # 6. Final model training
    if 'best_model = best_model.fit(X_train,y_train)' in source:
        new_source = []
        for line in cell['source']:
            if 'best_model = best_model.fit(X_train,y_train)' in line:
                new_source.append('best_model = best_model.fit(X_train_res, y_train_res)\n')
            else:
                new_source.append(line)
        cell['source'] = new_source

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
