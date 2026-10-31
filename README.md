# OptiCrop – Intelligent Crop Recommendation System 🌾

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Model](https://img.shields.io/badge/Model-Random%20Forest%20Classifier-forestgreen.svg)](https://scikit-learn.org/)
[![Accuracy](https://img.shields.io/badge/Accuracy-99.55%25-brightgreen.svg)](#model-performance)
[![Interface](https://img.shields.io/badge/Interface-Streamlit%20Web%20App%20%2B%20CLI-orange.svg)](#usage)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle%20Crop%20Recommendation-blueviolet.svg)](#dataset)

**OptiCrop** is a machine learning-powered agricultural advisory platform designed to recommend the most optimal crop for cultivation based on precision soil chemistry and environmental climate conditions. By modeling the complex non-linear relationships between soil macronutrients, acidity, and weather parameters, OptiCrop empowers farmers, agronomists, and agricultural researchers to maximize crop yields, mitigate crop failure risks, and optimize fertilizer investments.

---

## 🌟 Key Features

- **Multi-Factor Precision Agronomy**: Evaluates 7 core agricultural determinants: Nitrogen ($N$), Phosphorus ($P$), Potassium ($K$), Temperature, Humidity, Soil pH, and Rainfall.
- **Trained Random Forest Classifier**: High-capacity ensemble model achieving **99.55% test accuracy** and **99.55% 5-fold cross-validation accuracy** across 22 crop categories.
- **Top-3 Ranked Recommendations with Confidence Scores**: Rather than a single opaque output, OptiCrop provides ranked probabilities and confidence percentages for primary and alternative crop choices.
- **Detailed Agronomic Knowledge Base**: Provides botanical names, growing seasons (Kharif, Rabi, Zaid), water requirements, optimum soil types, and practical field management guidance for all 22 crops.
- **Parameter Suitability Analysis**: Compares the user's soil and climate inputs against the statistical norms for the recommended crop, highlighting deviations and nutritional requirements.
- **Interactive Modern Streamlit Web UI**: Responsive web application with real-time sliders, pre-configured agricultural scenarios, dynamic charts, and batch prediction uploads.
- **Versatile Command Line Interface (CLI)**: Direct terminal execution, interactive step-by-step prompts, JSON output mode for API integrations, and batch CSV processing.

---

## 📊 Dataset Overview

OptiCrop utilizes the standard **Crop Recommendation Dataset** commonly benchmarked on Kaggle. The dataset contains **2,200 empirical field records** distributed evenly (100 samples per crop) across **22 distinct crop categories**.

### Dataset Features

| Feature Name | Agronomic Description | Measurement Unit | Typical Dataset Range |
| :--- | :--- | :--- | :--- |
| **`N`** | Nitrogen content in soil | $\text{kg/ha}$ (ratio index) | $0 - 140$ |
| **`P`** | Phosphorus content in soil | $\text{kg/ha}$ (ratio index) | $5 - 145$ |
| **`K`** | Potassium content in soil | $\text{kg/ha}$ (ratio index) | $5 - 205$ |
| **`temperature`** | Ambient temperature | ${^\circ}\text{C}$ | $8.8 - 43.7$ |
| **`humidity`** | Relative humidity | $\%$ | $14.3 - 99.9$ |
| **`ph`** | Soil pH acidity/alkalinity | Dimensionless | $3.5 - 9.9$ |
| **`rainfall`** | Seasonal precipitation / rainfall | $\text{mm}$ | $20.2 - 298.6$ |
| **`label`** | **Target variable**: Recommended crop | Categorical (22 classes) | — |

### Supported 22 Crop Categories

- **Cereals & Grains:** Rice, Maize
- **Pulses & Legumes:** Chickpea, Kidney Beans, Pigeonpeas, Moth Beans, Mung Bean, Black Gram, Lentil
- **Fruits & Horticulture:** Banana, Mango, Grapes, Apple, Orange, Papaya, Pomegranate, Watermelon, Muskmelon
- **Commercial & Plantation:** Cotton, Jute, Coconut, Coffee

---

## 🔬 Model Architecture & Training

The core prediction engine uses a **Random Forest Classifier**, an ensemble learning method that constructs an uncorrelated forest of randomized decision trees at training time.

### Why Random Forest?
1. **Handles Non-Linear Agronomic Thresholds**: Plants have non-linear physiological thresholds (e.g., rice requires standing water $>200\text{ mm}$, whereas legumes rot in excessive moisture). Decision tree splits naturally represent these step-function bounds.
2. **Robust Against Outliers and Collinearity**: Bagging (bootstrap aggregating) mitigates overfitting and stabilizes variance.
3. **Calibrated Probability Distributions**: Enables multi-class probability extraction (`predict_proba`) to surface runner-up crop alternatives.

### Training Configuration
- **Estimators ($n$)**: 100 decision trees
- **Split Criterion**: Gini Impurity ($I_G(p) = 1 - \sum_{i=1}^{C} p_i^2$)
- **Validation**: 80/20 Stratified Train-Test Split + 5-Fold Stratified Cross-Validation
- **Random Seed**: 42 (fully reproducible)

### Model Performance

| Metric | Score |
| :--- | :--- |
| **Test Set Accuracy** | **99.55%** |
| **5-Fold Cross-Validation Accuracy** | **99.55% ($\pm 0.32\%$)** |
| **Weighted Precision** | **0.9957** |
| **Weighted Recall** | **0.9955** |
| **Weighted F1-Score** | **0.9955** |

### Feature Importance (Gini Importance)

Feature ranking demonstrates that precipitation and atmospheric moisture play the most decisive role in determining crop suitability, followed closely by potassium and phosphorus soil content:

```text
  1. Rainfall          : 23.0%
  2. Humidity          : 22.4%
  3. Potassium (K)     : 17.5%
  4. Phosphorus (P)    : 15.1%
  5. Nitrogen (N)      :  9.6%
  6. Temperature       :  7.2%
  7. Soil pH           :  5.1%
```

---

## 📁 Project Directory Structure

```text
Project/
├── .venv/                         # Python virtual environment
├── data/
│   ├── Crop_recommendation.csv     # Kaggle 2,200-sample dataset
│   ├── sample_test_batch.csv      # Sample batch input CSV
│   └── sample_test_predictions.csv# Sample batch predictions output
├── models/
│   ├── crop_rf_model.joblib       # Serialized Random Forest bundle & metadata
│   ├── model_metrics.json         # Evaluation metrics & classification report
│   ├── confusion_matrix.png       # 22x22 confusion matrix chart
│   └── feature_importance.png     # Bar chart of feature importance
├── src/
│   ├── __init__.py
│   ├── crop_info.py               # Agronomic database (22 crops metadata & advice)
│   ├── predict.py                 # CropRecommender inference engine
│   └── train.py                   # Automated ML training & evaluation script
├── tests/
│   └── test_opticrop.py           # Unit test suite (6 tests)
├── app.py                         # Streamlit interactive Web Application
├── cli.py                         # Command Line Interface (single/batch/JSON)
├── requirements.txt               # Dependencies
└── README.md                      # Comprehensive documentation
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13 installed on Windows, macOS, or Linux.

### 2. Clone or Navigate to the Project Directory
```powershell
cd c:\Users\hi\Desktop\Project
```

### 3. Activate the Virtual Environment
On Windows:
```powershell
.\.venv\Scripts\Activate.ps1
```
*(Or create a new venv with `python -m venv .venv` and run `pip install -r requirements.txt`)*

### 4. (Optional) Re-train the Model
The model artifact is already trained and saved in `models/crop_rf_model.joblib`. To retrain:
```powershell
.\.venv\Scripts\python.exe src\train.py
```

### 5. Run the Test Suite
```powershell
.\.venv\Scripts\python.exe -m unittest tests/test_opticrop.py
```

---

## 💻 How to Use OptiCrop

### A. Launch the Streamlit Web Application

To open the interactive web dashboard in your browser:
```powershell
.\.venv\Scripts\streamlit.exe run app.py
```

The application opens automatically at `http://localhost:8501`:
1. **Soil & Climate Sliders**: Adjust Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Soil pH, and Rainfall.
2. **Quick Presets**: Select scenarios such as *Rice (Monsoon Paddy)*, *Apple (Temperate Orchard)*, *Watermelon (Summer)*, *Cotton Belt*, or *Coffee Plantation*.
3. **Primary Recommendation Card**: Displays crop name, icon, scientific name, and confidence score.
4. **Candidate Crop Breakdown**: Displays top-3 alternatives with probability distribution charts.
5. **Suitability Parameter Table**: Side-by-side comparison between your input and ideal crop ranges.
6. **Batch CSV Upload**: Upload any farm CSV and download processed recommendations instantly.

---

### B. Command-Line Interface (CLI)

#### 1. Single Direct Prediction (e.g. Rice Conditions)
```powershell
.\.venv\Scripts\python.exe cli.py --nitrogen 90 --phosphorus 42 --potassium 43 --temperature 21.0 --humidity 82.0 --ph 6.5 --rainfall 202.0
```

**Output:**
```text
============================================================
  RECOMMENDED CROP: 🌾 RICE (Rice (Paddy))
  Confidence Score : 90.00%
  Category        : Cereal / Grain
  Botanical Name  : Oryza sativa
  Optimal Season  : Kharif (Monsoon: June – November)
  Water Need      : High (Standing water 5–10 cm during vegetative stage, 1500–2500 mm overall)
  Ideal Soil      : Clayey, alluvial, or heavy loams with high water-retention capacity.
============================================================

 Agronomic Advice:
  Ensure proper puddling before transplanting to reduce percolation losses.
  Apply nitrogen in 3 split doses (basal, tillering, panicle initiation) to maximize grain yield.

 Top Alternative Recommendations:
  #1 Rice            | Confidence:  90.00% | Cereal / Grain
  #2 Jute            | Confidence:  10.00% | Fiber / Commercial
  #3 Pomegranate     | Confidence:   0.00% | Fruit / Horticulture
============================================================
```

#### 2. Interactive Step-by-Step Prompt
Simply run `cli.py` without arguments:
```powershell
.\.venv\Scripts\python.exe cli.py --interactive
```

#### 3. JSON Output (for API integration or microservices)
```powershell
.\.venv\Scripts\python.exe cli.py -n 20 -p 130 -k 200 -t 22.0 -u 92.0 --ph 6.0 -r 110.0 --json
```

#### 4. Batch CSV Processing
```powershell
.\.venv\Scripts\python.exe cli.py --batch data/sample_test_batch.csv --output my_recommendations.csv
```

---

## 🔮 Future Enhancements

As noted in the project roadmap:
1. **Soil Physical Characteristics**: Incorporating soil texture percentages (sand, silt, clay) and bulk density.
2. **Economic & Market Price Integration**: Factoring in real-time mandi prices, minimum support prices (MSP), and yield-per-hectare profitability.
3. **Automated Weather & Geolocation Services**: Utilizing GPS coordinates to fetch historical climate averages and 14-day rainfall forecasts via weather APIs.
4. **Satellite Imagery / NDVI**: Coupling soil recommendations with Sentinel-2 / Landsat normalized difference vegetation indices.

---

## 📜 License
This project is open-source under the MIT License.
