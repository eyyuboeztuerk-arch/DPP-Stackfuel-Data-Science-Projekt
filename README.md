# Portfolio Projekt: 🫀 Cardiovascular Disease Prediction

Vorhersage des Risikos kardiovaskulärer Erkrankungen anhand klinischer und demografischer Merkmale – mit Fokus auf klinische Interpretierbarkeit, Validierung und Bias-Analyse.


## 📊 Projektübersicht

**Problemstellung:**  
Kardiovaskuläre Erkrankungen (CVD) gehören weltweit zu den häufigsten Todesursachen. Eine frühzeitige Risikoidentifikation kann präventive Maßnahmen ermöglichen und die Patientenversorgung verbessern. Dieses Projekt nutzt Machine Learning, um CVD-Risiken auf Basis klinischer Daten vorherzusagen.

**Ziel:**  
Entwicklung eines validen, kalibrierten Klassifikationsmodells zur Vorhersage von kardiovaskulärem Risiko. Schwerpunkt liegt auf **klinischer Interpretierbarkeit, Feature Importance und Bias-Analyse** um sowohl Data-Science-Kompetenz als auch medizinische Fachkenntnis zu demonstrieren.

**Methoden:**  
Geplant sind folgende Methoden:  
• Explorative Datenanalyse (EDA) mit medizinischem Fokus  
• Feature Engineering (BMI-Kategorien, Blutdruckgruppen)  
• Klassifikationsmodelle: Logistische Regression, Random Forest, Gradient Boosting (XGBoost/LightGBM)  
• Evaluation: ROC-AUC, PR-AUC, Calibration Plots, SHAP-basierte Explainability

## 🎯 Key Findings

<!-- Hier deine wichtigsten Erkenntnisse in 3-5 Bullet Points -->
- 📈 **Erkenntnis 1:** Kurze Beschreibung
- 🔍 **Erkenntnis 2:** Kurze Beschreibung  
- 💡 **Erkenntnis 3:** Kurze Beschreibung

## 📁 Repository Struktur

```
├── data/
│   ├── raw/                    # Originaldaten
│   └── processed/              # Bereinigte Daten
├── notebooks/                  # Jupyter Notebooks
│   └── 01_exploration.ipynb    # Datenexploration
├── src/dpp                     # Python Module
├── test/                       # Unit Tests
├── pyproject.toml              # Projektkonfiguration
└── docs/                       # Zusätzliche Dokumentation
```

## 🔧 Verwendete Technologien

**Programmiersprachen:**  
• Python 3.10+

**Libraries & Frameworks:**  
• **Data Processing**: pandas, numpy  
• **Visualisierung**: matplotlib, seaborn  
• **Machine Learning**: scikit-learn

**Tools:**  
• Jupyter Notebook / JupyterLab  
• Git & GitHub (Versionskontrolle)  
• UV (Python Paketmanager)  
• Visual Studio Code

## 📊 Daten

**Datenquelle:**  
[Kaggle (Cardiovascular Disease dataset)](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

**Datensatz-Größe:**  
• **70.000 Beobachtungen** (Patient:innen)  
• **11 Features**, 1 Zielvariable

**Wichtige Features:**  
• **Demografisch**: Alter, Geschlecht, Größe, Gewicht  
• **Klinisch**: Systolischer/Diastolischer Blutdruck (*ap_hi*, *ap_lo*), Cholesterin, Glukose  
• **Lifestyle**: Rauchen, Alkoholkonsum, körperliche Aktivität  
• **Zielvariable**: *cardio* (0 = kein Risiko, 1 = erhöhtes CVD-Risiko)  

## 🤖 Methodik

### Data Preprocessing
<!-- Kurze Beschreibung deiner Datenbereinigung -->

### Modeling Approach  
<!-- Welche Modelle hast du getestet? -->

### Evaluation
<!-- Wie hast du die Ergebnisse bewertet? -->

## 📈 Ergebnisse

**Model Performance:**
<!-- Deine besten Metriken (Accuracy, RMSE, etc.) -->

**Wichtigste Visualisierungen:**
<!-- Verweis auf Key-Plots in deinen Notebooks -->

## 🚀 Reproduzierbarkeit

### Setup
```bash
# Repository klonen
git clone https://github.com/eyyuboeztuerk-arch/DPP-Stackfuel-Data-Science-Projekt.git
cd DPP-Stackfuel-Data-Science-Projekt

# Dependencies installieren
uv sync
```

### Ausführung
```bash
# Notebooks in dieser Reihenfolge ausführen:
# 1. notebooks/01_exploration.ipynb
# 2. notebooks/02_preprocessing.ipynb  
# 3. notebooks/03_modeling.ipynb
# 4. notebooks/04_results.ipynb
```


## 🎓 Über dieses Projekt

**Kontext:**  
Dieses Projekt entsteht im Rahmen des **StackFuel Portfolio Projekt Kurses**. Mit diesem Projekt demonstriere ich den Übergang meiner Kenntnisse als **Biostatistiker in klinischen Studien** zu **angewandtem Data Science (im Gesundheitswesen)**.

**Zeitraum:**  
29.09.2025 - 17.10.2025

**Autor:**  
Eyyub Öztürk  
  Biostatistiker (M.Sc.) mit mehrjähriger Erfahrung in klinischen Studien, nun mit zusätzlicher Spezialisierung auf Data Science

## 📞 Kontakt

**GitHub:** [@DeinUsername](https://github.com/DeinUsername)  
**E-Mail:** deine.email@beispiel.de  
**LinkedIn:** [Dein Profil](https://linkedin.com/in/dein-profil)

## 🙏 Danksagungen

<!-- Hier kannst du Personen oder Ressourcen erwähnen, die dir geholfen haben -->

---

**⭐ Wenn dir dieses Projekt gefällt, gib gerne einen Star!**
