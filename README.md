# Portfolio Projekt: 🫀 Cardiovascular Disease Risk Prediction

Vorhersage des Risikos kardiovaskulärer Erkrankungen anhand von Lifestyle-, Gesundheits- und demografischen Merkmalen mit Fokus auf klinische Interpretierbarkeit, Validierung und Bias-Analyse.


## 📊 Projektübersicht

**Problemstellung:**  
Kardiovaskuläre Erkrankungen (CVD) gehören weltweit zu den häufigsten Todesursachen. Eine frühzeitige Risikoidentifikation kann präventive Maßnahmen ermöglichen und die Patientenversorgung verbessern. Dieses Projekt nutzt Machine Learning, um CVD-Risiken auf Basis von Gesundheits-, Lifestyle- und Ernährungsdaten vorherzusagen.

**Ziel:**  
Entwicklung eines validen, kalibrierten Klassifikationsmodells zur Vorhersage von kardiovaskulärem Risiko. Schwerpunkt liegt auf **klinischer Interpretierbarkeit, Feature Importance und Bias-Analyse** um sowohl Data-Science-Kompetenz als auch biostatistische Fachkenntnis zu demonstrieren.

**Methoden:**  
Geplant sind folgende Methoden:  
• Explorative Datenanalyse (EDA) mit medizinischem Fokus  
• Feature Engineering (BMI-Kategorien, Gesundheitsindizes, Lifestyle-Scores)  
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
[Kaggle – Cardiovascular Diseases Risk Prediction Dataset](https://www.kaggle.com/datasets/alphiree/cardiovascular-diseases-risk-prediction-dataset)  
**Originaldatenquelle:** CDC Behavioral Risk Factor Surveillance System (BRFSS) 2021

**Lizenz:**  
Public Domain (CDC-Daten)

**Datensatz-Größe:**  
• **308.854 Beobachtungen** (Befragte aus den USA)
• **19 Features**, 1 Zielvariable

**Wichtige Features:**  
• **Demografisch:** Alter (Kategorien: 18-24 bis 80+), Geschlecht, Größe, Gewicht, BMI  
• **Gesundheitsstatus:** Allgemeiner Gesundheitszustand, letzte Vorsorgeuntersuchung  
• **Chronische Erkrankungen:** Diabetes, Arthritis, Hautkrebs, andere Krebsarten, Depression  
• **Lifestyle-Faktoren:** Rauchen, Alkoholkonsum, körperliche Aktivität  
• **Ernährung:** Obst-, Gemüse- und Kartoffelkonsum (Portionen/Monat)  
• **Zielvariable:** `Heart_Disease` (0 = keine Herzerkrankung, 1 = Herzerkrankung diagnostiziert)

**Datenqualität:**  
• Offizielle CDC-Erhebung mit standardisiertem Erhebungsprotokoll  
• Repräsentative Stichprobe der US-Bevölkerung  
• Keine fehlenden Werte im bereinigten Datensatz  
• Umfassende Dokumentation verfügbar

## 🤖 Methodik

### 🔬 Hypothesen

1. **Alter und chronische Erkrankungen** sind die dominanten Risikofaktoren für Herzerkrankungen
2. **Lifestyle-Faktoren** (Rauchen, Bewegung, Ernährung) tragen signifikant zur Modellleistung bei
3. **BMI und allgemeiner Gesundheitszustand** zeigen starke Korrelation mit CVD-Risiko
4. Lineare Modelle (Logistische Regression) sind interpretierbarer, aber weniger performant als Ensemble-Methoden (Random Forest, XGBoost)
5. **Ernährungsmuster** (Obst/Gemüse vs. frittierte Kartoffeln) haben messbaren Einfluss auf CVD-Risiko

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
