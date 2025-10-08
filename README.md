# Portfolio Projekt: Diabetes Health Indicators: Binäre Klassifikation des Diabetesrisikos

Dieses Projekt befasst sich mit der Vorhersage des Diabetes-Status anhand von Gesundheits-, Lifestyle- und demografischen Merkmalen, mit Fokus auf klinische Interpretierbarkeit, valide Evaluation und Bias-Analyse.


## 📊 Projektübersicht

**Problemstellung:**  
Diabetes mellitus ist eine der häufigsten chronischen Erkrankungen weltweit. Eine frühzeitige Risikoidentifikation (kein Diabetes vs. Prädiabetes/Diabetes) ermöglicht gezielte Prävention und Versorgung. Dieses Projekt nutzt den Kaggle-Datensatz „Diabetes Health Indicators (Binary)“ (BRFSS 2015), um prädiktive Modelle für den binären Diabetes-Status zu entwickeln.

**Ziel:**  
Dieses Projekt entwickelt ein binäres Klassifikationsmodell zur Vorhersage des Diabetesrisikos. Dabei liegt der Schwerpunkt auf klinisch nachvollziehbaren Merkmalen und einer transparenten Erklärbarkeit der Modelle. Die Leistungsfähigkeit wird sowohl insgesamt als auch differenziert in Subgruppen (z. B. nach Alter, Geschlecht und BMI-Kategorien) bewertet. Zudem werden potenzielle Bias- und Fairness-Aspekte systematisch untersucht und die Limitationen der Analysen klar dokumentiert.

**Methoden:**  
Geplant sind folgende Methoden:
• Explorative Datenanalyse (EDA) mit medizinischem Fokus
• Feature Engineering (z. B. BMI-Kategorien, aggregierte Risikoscores)
• Binäre Klassifikation: Logistische Regression, Random Forest
• Evaluation: ROC-AUC, Precision-Recall-AUC, F1 (macro/weighted), Balanced Accuracy
• Subgruppen-/Bias-Analyse (z. B. Altersgruppen, Geschlecht, BMI-Kategorien)

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
• Data Processing: pandas, numpy  
• Visualisierung: matplotlib, seaborn  
• Machine Learning: scikit-learn

**Tools:**  
• Jupyter Notebook / JupyterLab  
• Git & GitHub (Versionskontrolle)  
• UV (Python Paketmanager)  
• Visual Studio Code

## 📊 Daten

**Datenquelle:**  
• Kaggle: Diabetes Health Indicators (Binary)  
• Datei: diabetes_binary_health_indicators_BRFSS2015.csv  
• Link: [Diabetes Health Indicators (Binary)](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_health_indicators_BRFSS2015.csv)  

**Lizenz:**  
Public Domain (CDC-Daten). Hinweise auf Kaggle/CDC beachten.

**Datensatz-Größe:**  
• **253.680 Beobachtungen** (BRFSS-Stichprobe)  
• **21 Features**, 1 Zielvariable  
• Binärer Zielstatus (0/1)

**Wichtige Features:**  
Auszug:  
• Demografisch: Age (kategorisiert), Sex, Education, Income, BMI  
• Gesundheitsstatus/Komorbiditäten: GenHlth, MentHlth, PhysHlth, DiffWalk, HighBP, HighChol, HeartDiseaseorAttack, Stroke  
• Lifestyle/Versorgung: Smoker, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, CholCheck  

**Datenqualität:**  
• Offizielle CDC-Erhebung  
• In diesem Kaggle-Release typischerweise bereinigt; fehlende Werte sind selten  
• Details siehe Kaggle-Beschreibung und CDC-Codebooks

## 🤖 Methodik

### 🔬 Hypothesen

• Alter, BMI und kardiometabolische Komorbiditäten sind dominante Risikofaktoren; Lifestyle-Faktoren tragen substantiell zur Trennung 0 vs. 1 bei.  
• Logistische Regression ist gut interpretierbar; Baumverfahren/Boosting erreichen häufig höhere F1-/ROC-AUC-Werte.

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
