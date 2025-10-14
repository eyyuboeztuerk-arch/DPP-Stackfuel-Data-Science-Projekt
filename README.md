# Portfolio Project: Diabetes Health Indicators — Binary Classification of Diabetes Risk

This project focuses on predicting diabetes status based on health, lifestyle, and demographic features, emphasizing clinical interpretability, valid evaluation, and bias analysis.


## 📊 Project Overview

**Problem Statement:**  
Diabetes mellitus is one of the most common chronic diseases worldwide. Early risk identification (no diabetes vs. prediabetes/diabetes) enables targeted prevention and care. This project uses the Kaggle dataset “Diabetes Health Indicators (Binary)” (BRFSS 2015) to develop predictive models for binary diabetes status.

**Objective:**  
Develop a binary classification model to predict diabetes risk, focusing on clinically interpretable features and transparent model explainability. Performance is evaluated overall and stratified by subgroups (e.g., age, sex, BMI categories). Potential bias and fairness aspects are systematically analyzed, and limitations are clearly documented.

**Methods:**
- Exploratory Data Analysis (EDA) with medical focus  
- Feature engineering (e.g., BMI categories, aggregated risk scores)  
- Binary classification: Logistic Regression, Random Forest, XGBoost, SVM, Neural Networks, etc.  
- Evaluation: ROC-AUC, Precision-Recall AUC, F1-score, Balanced Accuracy  
- Subgroup and bias analysis (age groups, sex, BMI categories)  
- Decision Curve Analysis (DCA) for clinical utility assessment  

**Limitation:**
- The binary target variable combines both prediabetes and diabetes cases into a single positive class (class 1).  
- This limits the granularity of risk stratification and clinical interpretation.  

**Future Work:**  
Plan to develop a comparative portfolio project using the related Kaggle dataset with a three-class target variable:  
- Class 0: No diabetes  
- Class 1: Prediabetes  
- Class 2: Diabetes

This will enable multi-class classification and more nuanced risk prediction.

## 🎯 Key Findings

<!-- Hier deine wichtigsten Erkenntnisse in 3-5 Bullet Points -->
- 📈 **Finding 1:** XGBoost achieved the best overall performance with an F1-score of approximately 0.47 and ROC-AUC around 0.82.
- 🔍 **Finding 2:** SVM and Logistic Regression showed high sensitivity (recall ~0.76), important for detecting diabetes cases.
- 💡 **Finding 3:** Optimized thresholds (e.g., 0.26 for XGBoost) significantly improve diabetes detection compared to the default 0.5 threshold.
- ⚖️ **Finding 4:** Decision Curve Analysis confirms the clinical benefit of the models compared to “treat all” or “treat none” strategies.
- 📊 **Finding 5:** Hypertension (by far), BMI, age, and cardiovascular disease are one of the most important predictors of diabetes risk.

## 📁 Repository Struktur

```  
├── data/  
│   ├── raw/                    # Original data  
│   └── processed/              # Cleaned data  
├── notebooks/                  # Jupyter notebooks  
│   ├── 01_exploration.ipynb    # Data exploration  
│   ├── 02_preprocessing.ipynb  # Data preprocessing     
│   ├── 03_modeling.ipynb       # Modeling  
│   └── 04_results.ipynb        # Results visualization  
├── src/dpp                     # Python modules  
├── models/                     # Saved models and results (.pkl)  
├── test/                       # Unit tests  
├── pyproject.toml              # Project configuration  
└── docs/                       # Additional documentation
```

## 🔧 Technologies Used

**Programming Languages:**
- Python 3.10+  

**Libraries & Frameworks:**
- Data Processing: pandas, numpy  
- Visualization: matplotlib, seaborn  
- Machine Learning: scikit-learn, xgboost  

**Tools:**
- Jupyter Notebook / JupyterLab  
- Git & GitHub (version control)  
- UV (Python package manager)  
- Visual Studio Code

## 📊 Daten

**Data Source:**  
Kaggle: Diabetes Health Indicators (Binary)  
File: diabetes_binary_health_indicators_BRFSS2015.csv  
Link: [Diabetes Health Indicators (Binary)](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_health_indicators_BRFSS2015.csv)  

**License:**  
Public Domain (CDC data). See Kaggle/CDC for details.

**Dataset Size:**
- 253,680 observations (BRFSS-Stichprobe)
- 21 features, 1 binary target variable  

**Key Features:**
- Demographics: Age (categorized), Sex, Education, Income, BMI
- Health status/comorbidities: GenHlth, MentHlth, PhysHlth, DiffWalk, HighBP, HighChol, HeartDiseaseorAttack, Stroke
- Lifestyle/access: Smoker, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, CholCheck  

**Data Quality:**
- Official CDC survey data
- Cleaned dataset with rare missing values
- See Kaggle description and CDC codebooks for details  

## 🤖 Methodology

### 🔬 Hypotheses

- Age, BMI, and cardiometabolic comorbidities are dominant risk factors; lifestyle factors contribute substantially to class separation.
- Logistic regression offers interpretability; tree-based and boosting methods often achieve higher F1 and ROC-AUC.  

### Data Preprocessing
<!-- Kurze Beschreibung deiner Datenbereinigung -->
- Cleaning and encoding missing values
- Feature engineering (BMI categories, age groups)
- Handling class imbalance (SMOTE)  

### Modeling Approach
<!-- Welche Modelle hast du getestet? -->
- Models: Logistic Regression, Random Forest, XGBoost, SVM, Neural Networks
- Hyperparameter tuning with RandomizedSearchCV
- Threshold optimization to maximize F1-score  

### Evaluation
<!-- Wie hast du die Ergebnisse bewertet? -->
- Metrics: ROC-AUC, Precision, Recall, F1-score, Accuracy, Cross-validation
- Decision Curve Analysis (DCA) for clinical utility
- Subgroup analyses by age, sex, BMI  

## 📈 Results  

**Model Performance:**
<!-- Deine besten Metriken (Accuracy, RMSE, etc.) -->
- XGBoost: F1 ≈ 0.47, ROC-AUC ≈ 0.82, optimal threshold ≈ 0.26
- SVM & Logistic Regression: high recall (~0.76), important for diabetes detection
- Neural Network: F1 ≈ 0.42, balanced precision and recall  

**Key Visualizations:**
<!-- Verweis auf Key-Plots in deinen Notebooks -->
- ROC and Precision-Recall curves for all models
- Feature importance (XGBoost, Random Forest)
- Decision Curve Analysis (DCA)
- Confusion matrix at optimal threshold  

## Confusion Matrix and Classification Report Explanation

The confusion matrix for the best model (XGBoost, threshold 0.261) on the test set is:

|                      | Predicted Negative (0) | Predicted Positive (1) |
|----------------------|------------------------|------------------------|
| Actual Negative (0)   | 31,202 (True Negative) | 7,674 (False Positive) |
| Actual Positive (1)   | 2,510 (False Negative) | 4,509 (True Positive)  |

- **True Positives (TP):** 4,509 diabetes cases correctly identified.  
- **True Negatives (TN):** 31,202 non-diabetes cases correctly identified.  
- **False Positives (FP):** 7,674 non-diabetes cases incorrectly predicted as diabetes.  
- **False Negatives (FN):** 2,510 diabetes cases missed by the model.

### Performance metrics derived:

- **Precision (class 1):** 0.37 — Of all predicted diabetes cases, 37% are correct.  
- **Recall (Sensitivity):** 0.64 — The model detects 64% of all actual diabetes cases.  
- **F1-score (class 1):** 0.47 — Harmonic mean of precision and recall.  
- **Accuracy:** 0.78 — Overall correct predictions.

## 🚀 Reproducibility

### Setup
```bash
# Repository klonen
git clone https://github.com/eyyuboeztuerk-arch/DPP-Stackfuel-Data-Science-Projekt.git
cd DPP-Stackfuel-Data-Science-Projekt

# Dependencies installieren
uv sync
```

### Execution
```bash
# Notebooks in dieser Reihenfolge ausführen:
# 1. notebooks/01_exploration.ipynb
# 2. notebooks/02_preprocessing.ipynb  
# 3. notebooks/03_modeling.ipynb
# 4. notebooks/04_results.ipynb
```


## 🎓 About this Project

**Context:**  
This project was developed as part of the **StackFuel Portfolio Project Course**. It demonstrates my transition from a **biostatistician in clinical trials** to an applied **data scientist (in healthcare)**.

**Period:**  
September 29, 2025 - October 17, 2025

**Author:**  
Eyyub Öztürk  
*Biostatistician (M.Sc.) with several years of experience in clinical trials, now specialized in data science.*

## 📞 Contact

**GitHub:** [@DeinUsername](https://github.com/DeinUsername)  
**E-Mail:** deine.email@beispiel.de  
**LinkedIn:** [Dein Profil](https://linkedin.com/in/dein-profil)

## 🙏 Acknowledgments  

<!-- Hier kannst du Personen oder Ressourcen erwähnen, die dir geholfen haben -->
Thanks to StackFuel, the community, and everyone who supported me during this project.

---

**⭐ If you like this project, please give it a star!**
