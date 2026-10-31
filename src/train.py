"""
OptiCrop - Model Training Pipeline
Trains a Random Forest Classifier on the Kaggle Crop Recommendation Dataset.
Outputs the serialized model, evaluation metrics, and feature importance charts.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score
)

def train_opticrop_model(data_path="data/Crop_recommendation.csv", model_dir="models"):
    os.makedirs(model_dir, exist_ok=True)
    
    print(f"Loading dataset from {data_path}...")
    df = pd.read_csv(data_path)
    
    feature_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    target_col = 'label'
    
    X = df[feature_cols]
    y = df[target_col]
    
    print(f"Dataset shape: {df.shape} (2200 samples, 22 crops, 7 features)")
    
    # Stratified Train-Test Split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")
    
    # Random Forest Classifier
    rf = RandomForestClassifier(
        n_estimators=100,
        criterion='gini',
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1
    )
    
    print("Training Random Forest Classifier...")
    rf.fit(X_train, y_train)
    
    # 5-Fold Stratified Cross Validation
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(rf, X, y, cv=cv, scoring='accuracy')
    print(f"5-Fold Cross Validation Accuracy: {cv_scores.mean() * 100:.2f}% (std: {cv_scores.std() * 100:.2f}%)")
    
    # Evaluation on Test Set
    y_pred = rf.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)
    test_f1 = f1_score(y_test, y_pred, average='weighted')
    test_prec = precision_score(y_test, y_pred, average='weighted')
    test_rec = recall_score(y_test, y_pred, average='weighted')
    
    print(f"Test Accuracy: {test_acc * 100:.2f}%")
    print(f"Weighted F1-Score: {test_f1:.4f}")
    print(f"Weighted Precision: {test_prec:.4f}")
    print(f"Weighted Recall: {test_rec:.4f}")
    
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_text = classification_report(y_test, y_pred)
    print("\nClassification Report:\n", report_text)
    
    # Feature Importances
    feature_importances = dict(zip(feature_cols, rf.feature_importances_))
    sorted_importances = sorted(feature_importances.items(), key=lambda item: item[1], reverse=True)
    print("\nFeature Importances:")
    for feat, imp in sorted_importances:
        print(f"  {feat:12s}: {imp:.4f} ({imp * 100:.1f}%)")
        
    # Crop statistical profiles (mean, min, max for each feature per crop)
    crop_profiles = {}
    for crop in df[target_col].unique():
        crop_df = df[df[target_col] == crop]
        crop_profiles[crop] = {
            col: {
                "mean": float(crop_df[col].mean()),
                "min": float(crop_df[col].min()),
                "max": float(crop_df[col].max()),
                "std": float(crop_df[col].std())
            }
            for col in feature_cols
        }
    
    # Serialize model and metadata package
    model_artifact = {
        "model": rf,
        "feature_names": feature_cols,
        "classes": sorted(list(rf.classes_)),
        "metrics": {
            "test_accuracy": float(test_acc),
            "test_f1": float(test_f1),
            "test_precision": float(test_prec),
            "test_recall": float(test_rec),
            "cv_accuracy_mean": float(cv_scores.mean()),
            "cv_accuracy_std": float(cv_scores.std()),
        },
        "feature_importances": {k: float(v) for k, v in feature_importances.items()},
        "crop_profiles": crop_profiles
    }
    
    model_path = os.path.join(model_dir, "crop_rf_model.joblib")
    joblib.dump(model_artifact, model_path)
    print(f"\nModel bundle saved to: {model_path}")
    
    # Save metrics JSON
    metrics_path = os.path.join(model_dir, "model_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump({
            "test_accuracy": float(test_acc),
            "test_f1": float(test_f1),
            "test_precision": float(test_prec),
            "test_recall": float(test_rec),
            "cv_accuracy_mean": float(cv_scores.mean()),
            "cv_accuracy_std": float(cv_scores.std()),
            "feature_importances": {k: float(v) for k, v in sorted_importances},
            "classification_report": report_dict
        }, f, indent=4)
    print(f"Metrics saved to: {metrics_path}")
    
    # Generate Confusion Matrix Chart
    plt.figure(figsize=(14, 11))
    cm = confusion_matrix(y_test, y_pred, labels=rf.classes_)
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Greens',
        xticklabels=rf.classes_,
        yticklabels=rf.classes_
    )
    plt.title("Confusion Matrix - Crop Recommendation Random Forest", fontsize=14, pad=12)
    plt.xlabel("Predicted Crop", fontsize=12)
    plt.ylabel("Actual Crop", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    cm_path = os.path.join(model_dir, "confusion_matrix.png")
    plt.savefig(cm_path, dpi=200)
    plt.close()
    print(f"Confusion matrix plot saved to: {cm_path}")
    
    # Generate Feature Importance Chart
    plt.figure(figsize=(9, 5))
    feats, imps = zip(*sorted_importances)
    colors = sns.color_palette("viridis", len(feats))
    plt.barh(feats[::-1], imps[::-1], color=colors)
    plt.title("OptiCrop - Feature Importance (Random Forest Gini Importance)", fontsize=13)
    plt.xlabel("Importance Score", fontsize=11)
    plt.ylabel("Agricultural Feature", fontsize=11)
    plt.tight_layout()
    fi_path = os.path.join(model_dir, "feature_importance.png")
    plt.savefig(fi_path, dpi=200)
    plt.close()
    print(f"Feature importance plot saved to: {fi_path}")
    
    return model_artifact

if __name__ == "__main__":
    train_opticrop_model()
