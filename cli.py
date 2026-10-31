#!/usr/bin/env python3
"""
OptiCrop - Command Line Interface (CLI)
Provides single prediction, interactive prediction mode, and batch processing.
"""

import sys
import argparse
import json
import pandas as pd

# Handle Windows cp1252 terminal encoding gracefully
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from src.predict import CropRecommender, PARAM_CONSTRAINTS

def print_banner():
    banner = r"""
  ==============================================================
    🌾 OptiCrop: Intelligent Crop Recommendation System 🌾
    Machine Learning-Powered Agronomic Advisory Engine
  ==============================================================
    """
    print(banner)

def run_interactive(recommender: CropRecommender):
    print("\n--- Enter Soil and Climate Parameters ---")
    inputs = {}
    prompts = [
        ("N", "Nitrogen (N) content in soil (kg/ha)", 0.0, 140.0, 90.0),
        ("P", "Phosphorus (P) content in soil (kg/ha)", 5.0, 145.0, 42.0),
        ("K", "Potassium (K) content in soil (kg/ha)", 5.0, 205.0, 43.0),
        ("temperature", "Temperature (°C)", 5.0, 55.0, 21.0),
        ("humidity", "Relative Humidity (%)", 10.0, 100.0, 82.0),
        ("ph", "Soil pH (3.5 - 9.5)", 3.5, 10.0, 6.5),
        ("rainfall", "Rainfall (mm)", 10.0, 350.0, 202.0)
    ]
    
    for key, desc, min_v, max_v, default_v in prompts:
        while True:
            raw = input(f"Enter {desc} [default {default_v}]: ").strip()
            if not raw:
                inputs[key] = default_v
                break
            try:
                val = float(raw)
                inputs[key] = val
                break
            except ValueError:
                print("  Invalid numeric value. Please re-enter.")
                
    result = recommender.recommend(
        nitrogen=inputs["N"],
        phosphorus=inputs["P"],
        potassium=inputs["K"],
        temperature=inputs["temperature"],
        humidity=inputs["humidity"],
        ph=inputs["ph"],
        rainfall=inputs["rainfall"],
        top_k=3
    )
    
    display_recommendation(result)

def display_recommendation(result: dict):
    primary = result["primary_recommendation"]
    conf = result["primary_confidence_percent"]
    meta = result["primary_metadata"]
    
    print("\n" + "="*60)
    print(f"  RECOMMENDED CROP: {meta.get('icon', '🌱')} {primary.upper()} ({meta.get('common_name', primary)})")
    print(f"  Confidence Score : {conf:.2f}%")
    print(f"  Category        : {meta.get('category', 'N/A')}")
    print(f"  Botanical Name  : {meta.get('scientific_name', 'N/A')}")
    print(f"  Optimal Season  : {meta.get('growing_season', 'N/A')}")
    print(f"  Water Need      : {meta.get('water_requirement', 'N/A')}")
    print(f"  Ideal Soil      : {meta.get('soil_type', 'N/A')}")
    print("="*60)
    print("\n Agronomic Advice:")
    print(f"  {meta.get('agronomic_advice', 'N/A')}")
    
    print("\n Top Alternative Recommendations:")
    for rec in result["top_recommendations"]:
        print(f"  #{rec['rank']} {rec['crop'].capitalize():15s} | Confidence: {rec['confidence_percent']:6.2f}% | {rec['metadata'].get('category', '')}")
        
    if result.get("warnings"):
        print("\n Notes & Warnings:")
        for w in result["warnings"]:
            print(f"  ! {w}")
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="OptiCrop – Machine Learning Crop Recommendation CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--interactive", "-i", action="store_true", help="Launch interactive step-by-step prompt")
    parser.add_argument("--nitrogen", "-n", type=float, help="Nitrogen (N) soil content (kg/ha)")
    parser.add_argument("--phosphorus", "-p", type=float, help="Phosphorus (P) soil content (kg/ha)")
    parser.add_argument("--potassium", "-k", type=float, help="Potassium (K) soil content (kg/ha)")
    parser.add_argument("--temperature", "-t", type=float, help="Temperature in °C")
    parser.add_argument("--humidity", "-u", type=float, help="Relative humidity percentage (%)")
    parser.add_argument("--ph", type=float, help="Soil pH value (3.5 - 9.5)")
    parser.add_argument("--rainfall", "-r", type=float, help="Rainfall in mm")
    parser.add_argument("--top-k", type=int, default=3, help="Number of top crop recommendations (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--batch", type=str, help="Path to input CSV for batch prediction")
    parser.add_argument("--output", "-o", type=str, help="Output path for batch predictions CSV")

    args = parser.parse_args()
    
    recommender = CropRecommender()

    # Batch mode
    if args.batch:
        print(f"Processing batch file: {args.batch}")
        df = pd.read_csv(args.batch)
        res_df = recommender.batch_recommend(df)
        out_path = args.output if args.output else "batch_predictions_output.csv"
        res_df.to_csv(out_path, index=False)
        print(f"Saved {len(res_df)} predictions to: {out_path}")
        return

    # Interactive mode or missing parameters
    required_args = [args.nitrogen, args.phosphorus, args.potassium, args.temperature, args.humidity, args.ph, args.rainfall]
    if args.interactive or any(a is None for a in required_args):
        if not args.interactive and any(a is not None for a in required_args):
            print("Note: Incomplete parameters provided. Switching to interactive mode...")
        print_banner()
        run_interactive(recommender)
        return

    # Direct CLI execution
    result = recommender.recommend(
        nitrogen=args.nitrogen,
        phosphorus=args.phosphorus,
        potassium=args.potassium,
        temperature=args.temperature,
        humidity=args.humidity,
        ph=args.ph,
        rainfall=args.rainfall,
        top_k=args.top_k
    )

    if args.json:
        # Strip complex objects for pure JSON
        print(json.dumps(result, indent=2))
    else:
        print_banner()
        display_recommendation(result)

if __name__ == "__main__":
    main()
