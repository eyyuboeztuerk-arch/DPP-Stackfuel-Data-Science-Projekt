# Portfolio Projekt: Diabetes Health Indicators: Multi-Class Risk Prediction

Dieses Projekt befasst sich mit der Vorhersage des Diabetes-Status (0/1/2) anhand von Gesundheits-, Lifestyle- und demografischen Merkmalen mit Fokus auf klinische Interpretierbarkeit, Validierung und Bias-Analyse.


## 📊 Projektübersicht

**Problemstellung:**  
Diabetes mellitus ist eine der häufigsten chronischen Erkrankungen weltweit. Eine frühzeitige und differenzierte Risikoidentifikation (kein Diabetes vs. Prädiabetes vs. Diabetes) ermöglicht gezielte Prävention und Versorgung. Dieses Projekt nutzt den Kaggle-Datensatz „Diabetes Health Indicators“ (BRFSS 2015) zur Entwicklung prädiktiver Modelle für den dreistufigen Diabetes-Status.

**Ziel:**  
Entwicklung valider, kalibrierter Multiklassen-Modelle zur Vorhersage des Diabetes-Status mit drei Ausprägungen:  
  
• 0 = kein Diabetes  
• 1 = Prädiabetes  
• 2 = Diabetes  
  
Schwerpunkt: klinische Interpretierbarkeit, Feature Importance, Kalibrierung und Bias-/Subgruppen-Analysen.

**Methoden:**  
Geplant sind folgende Methoden:  
• Explorative Datenanalyse (EDA) mit medizinischem Fokus
• Feature Engineering (BMI-Kategorien, Lifestyle-Score)
• Multiklassen-Klassifikation: Logistische Regression, Random Forest
• Evaluation: ROC-AUC (One-vs-Rest), PR-AUC je Klasse, Macro-/Weighted-F1
• Subgruppen-/Bias-Analyse (z. B. Alter, Geschlecht)

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
Kaggle – Diabetes Health Indicators Dataset (Alex Teboul), BRFSS 2015.
Verwendete Datei: diabetes_012_health_indicators_BRFSS2015.csv
URL: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_012_health_indicators_BRFSS2015.csv

**Lizenz:**  
Public Domain (CDC-Daten). Hinweise auf Kaggle/CDC beachten.

**Datensatz-Größe:**  
• **254.000 Beobachtungen** (BRFSS-Stichprobe)
• **21 Features**, 1 Zielvariable
• Zielvariable: Diabetes_012 mit drei Ausprägungen (0/1/2)

**Wichtige Features:**  
• Demografisch: Alter (kategorisiert), Geschlecht, BMI
• Gesundheitsstatus/Komorbiditäten: Allgemeiner Gesundheitszustand, Hypertonie-/Cholesterin-Indikatoren, Depression, Arthritis, Krebs
• Lifestyle: Rauchen, Alkoholkonsum, körperliche Aktivität
• Zielvariable: Diabetes_012 (0 = kein Diabetes, 1 = Prädiabetes, 2 = Diabetes)

**Datenqualität:**  
• Offizielle CDC-Erhebung (standardisierte Telefonumfrage)
• In diesem Kaggle-Release i. d. R. bereinigt; fehlende Werte sind selten bzw. bereits behandelt
• Details siehe Kaggle-Beschreibung und CDC-Codebooks

## 🤖 Methodik

### 🔬 Hypothesen

• Alter, BMI und chronische Erkrankungen sind dominante Risikofaktoren; Lifestyle-Faktoren tragen substanziell zur Diskrimination zwischen 0/1/2 bei.
• Logistische Regression (Multinomial) ist interpretierbar; Gradient Boosting erreicht häufig bessere Macro-F1/PR-AUC.
• Kalibrierung pro Klasse ist entscheidend, insbesondere zur Trennung 0 vs. 1 (Prädiabetes).

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
  *Biostatistiker (M.Sc.) mit mehrjähriger Erfahrung in klinischen Studien, nun mit zusätzlicher Spezialisierung auf Data Science*

## 📞 Kontakt

**GitHub:** [@DeinUsername](https://github.com/DeinUsername)  
**E-Mail:** deine.email@beispiel.de  
**LinkedIn:** [Dein Profil](https://linkedin.com/in/dein-profil)

## 🙏 Danksagungen

<!-- Hier kannst du Personen oder Ressourcen erwähnen, die dir geholfen haben -->

---

**⭐ Wenn dir dieses Projekt gefällt, gib gerne einen Star!**
