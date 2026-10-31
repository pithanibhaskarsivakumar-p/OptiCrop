"""
OptiCrop Test Suite
Validates model predictions, input handling, metadata integrity, and batch execution.
"""

import unittest
import os
import pandas as pd
from src.predict import CropRecommender
from src.crop_info import CROP_DETAILS, get_crop_metadata

class TestOptiCrop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        model_path = os.path.join(os.path.dirname(__file__), "..", "models", "crop_rf_model.joblib")
        cls.recommender = CropRecommender(model_path=model_path)

    def test_model_loaded(self):
        self.assertIsNotNone(self.recommender.model)
        self.assertEqual(len(self.recommender.classes), 22)
        self.assertEqual(len(self.recommender.feature_names), 7)

    def test_rice_recommendation(self):
        # Rice conditions from typical dataset sample
        res = self.recommender.recommend(
            nitrogen=90, phosphorus=42, potassium=43,
            temperature=20.88, humidity=82.0, ph=6.5, rainfall=202.93
        )
        self.assertEqual(res["primary_recommendation"], "rice")
        self.assertGreater(res["primary_confidence"], 0.70)
        self.assertEqual(res["primary_metadata"]["scientific_name"], "Oryza sativa")

    def test_apple_recommendation(self):
        # Apple conditions (high P, high K, temperate)
        res = self.recommender.recommend(
            nitrogen=20, phosphorus=130, potassium=200,
            temperature=22.0, humidity=92.0, ph=6.0, rainfall=110.0
        )
        self.assertEqual(res["primary_recommendation"], "apple")
        self.assertGreater(res["primary_confidence"], 0.85)

    def test_coffee_recommendation(self):
        # Coffee conditions
        res = self.recommender.recommend(
            nitrogen=100, phosphorus=20, potassium=30,
            temperature=25.0, humidity=60.0, ph=6.7, rainfall=160.0
        )
        self.assertEqual(res["primary_recommendation"], "coffee")
        self.assertGreater(res["primary_confidence"], 0.80)

    def test_all_22_classes_metadata_exist(self):
        for crop in self.recommender.classes:
            meta = get_crop_metadata(crop)
            self.assertIn("common_name", meta)
            self.assertIn("scientific_name", meta)
            self.assertIn("category", meta)
            self.assertIn("water_requirement", meta)
            self.assertIn("soil_type", meta)

    def test_batch_recommendation(self):
        sample_df = pd.DataFrame([
            {"N": 90, "P": 42, "K": 43, "temperature": 20.88, "humidity": 82.0, "ph": 6.5, "rainfall": 202.93},
            {"N": 20, "P": 130, "K": 200, "temperature": 22.0, "humidity": 92.0, "ph": 6.0, "rainfall": 110.0}
        ])
        batch_res = self.recommender.batch_recommend(sample_df)
        self.assertEqual(len(batch_res), 2)
        self.assertIn("recommended_crop", batch_res.columns)
        self.assertIn("confidence_score", batch_res.columns)
        self.assertEqual(batch_res.iloc[0]["recommended_crop"], "rice")
        self.assertEqual(batch_res.iloc[1]["recommended_crop"], "apple")

if __name__ == "__main__":
    unittest.main()
