# Wireframe Document
## Erasmus Mundus Scholarship Prediction Platform

**Document Version Control**
| Date Issued | Version | Description |
| :--- | :--- | :--- |
| **05th August 2026** | 1.0 | First Draft of Complete Wireframe Document |

---

## 1. Homepage & Dashboard

The homepage contains the welcome text and an overview of the system. It consists of the following navigation options on the sidebar:
*   **Dashboard** (EDA Insights)
*   **Predict Chances** (ML Model Input)
*   **Historical Data** (Dataset View)

### 1.1 Real-Time Dashboard View

*(Note: The Dashboard will display real-time interactive charts similar to the visualizations we generated in `1_EDA_Scholarship.ipynb` using Matplotlib and Seaborn.)*

```text
+-----------------------------------------------------------------------------------+
|  [Logo] Scholarship Predictor             [Home] [Predict] [About]  [User Profile]|
+-----------------------------------------------------------------------------------+
|                                                                                   |
|   +-----------------------+     +---------------------------------------------+   |
|   |                       |     |                                             |   |
|   |  Navigation Menu      |     |   📊 REAL-TIME EDA DASHBOARD                |   |
|   |                       |     |                                             |   |
|   |  > Dashboard          |     |   +-----------------+  +------------------+ |   |
|   |    (Active)           |     |   | Awarded: 27%    |  | Top Countries    | |   |
|   |                       |     |   | Denied:  73%    |  | 1. India         | |   |
|   |  > Predict Chances    |     |   +-----------------+  +------------------+ |   |
|   |                       |     |                                             |   |
|   |  > Historical Data    |     |   +---------------------------------------+ |   |
|   |                       |     |   |       [ Histogram: CGPA vs Award ]    | |   |
|   |  > Settings           |     |   |           _                         | |   |
|   |                       |     |   |          / \                        | |   |
|   +-----------------------+     |   |         /   \                       | |   |
|                                 |   +---------------------------------------+ |   |
|                                 +---------------------------------------------+   |
+-----------------------------------------------------------------------------------+
```

---

## 2. Predict Chances (Model Inference)

This section allows the user to input their academic metrics and receive a real-time prediction from our Scikit-Learn Random Forest model.

### 2.1 Input Data Form

```text
+-----------------------------------------------------------------------------------+
|                                                                                   |
|   +-----------------------+     +---------------------------------------------+   |
|   |  Navigation Menu      |     |                                             |   |
|   |                       |     |   🎯 PREDICT YOUR SCHOLARSHIP CHANCES       |   |
|   |  > Dashboard          |     |                                             |   |
|   |                       |     |   Please enter your academic metrics:       |   |
|   |  > Predict Chances    |     |                                             |   |
|   |    (Active)           |     |   CGPA (out of 4.0):  [ 3.85 ]              |   |
|   |                       |     |                                             |   |
|   |  > Historical Data    |     |   GRE Score:          [ 320  ]              |   |
|   |                       |     |                                             |   |
|   |                       |     |   Internship Exp?     (o) Yes   ( ) No      |   |
|   +-----------------------+     |                                             |   |
|                                 |   Research Exp?       (o) Yes   ( ) No      |   |
|                                 |                                             |   |
|                                 |   Graduation Year:    [ 2024 ▼]             |   |
|                                 |                                             |   |
|                                 |            [ PREDICT NOW ]                  |   |
|                                 +---------------------------------------------+   |
+-----------------------------------------------------------------------------------+
```

---

## 3. Prediction Result View

Once the user clicks "Predict Now", the data is fed through our `preprocessor.pkl` and `model.pkl`. The result is displayed immediately.

```text
+-----------------------------------------------------------------------------------+
|                                                                                   |
|   +-----------------------+     +---------------------------------------------+   |
|   |  Navigation Menu      |     |                                             |   |
|   |                       |     |   🎉 YOUR PREDICTION RESULTS                |   |
|   |  > Dashboard          |     |                                             |   |
|   |                       |     |   +---------------------------------------+ |   |
|   |  > Predict Chances    |     |   |                                       | |   |
|   |    (Active)           |     |   |      SUCCESS PROBABILITY: 88%         | |   |
|   |                       |     |   |      Status: HIGHLY LIKELY            | |   |
|   |                       |     |   |                                       | |   |
|   +-----------------------+     |   +---------------------------------------+ |   |
|                                 |                                             |   |
|                                 |   💡 AI Insights on your profile:           |   |
|                                 |   - Excellent CGPA (+12% boost)             |   |
|                                 |   - Research Experience detected (+25%)     |   |
|                                 |   - Fresh Graduate status (+5% boost)       |   |
|                                 +---------------------------------------------+   |
+-----------------------------------------------------------------------------------+
```

---

## 4. Historical Data

Here, users can monitor raw data (anonymized) with the help of a data grid (similar to a pandas dataframe view). This helps build trust in the model by showing actual past accepted/denied profiles.

*   Displays a Paginated Table of `Graduate.csv`.
*   Users can filter by "Awarded = Yes" to see what a successful profile looks like.

---
*End of Wireframe Document*
