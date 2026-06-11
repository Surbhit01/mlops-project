import pandas as pd
import numpy as np

def simulate_drift(input_path: str, output_path: str, random_state: int = 42):
    """
    Simulate data drift on the AttritionGuard dataset.
    
    Story: 6 months after deployment, the company went through
    a restructuring. Employees are working more overtime,
    earning less, and are less satisfied.
    """
    np.random.seed(random_state)
    
    df = pd.read_csv(input_path)
    drifted = df.copy()
    n = len(drifted)

    print(f"Original dataset shape: {df.shape}")
    print("\nSimulating drift...")

    # ── Drift 1: OverTime ──────────────────────────────────────────
    # Originally ~30% overtime. Now ~60% — restructuring means
    # fewer people doing more work
    original_overtime = drifted["OverTime"].mean()
    drifted["OverTime"] = np.random.choice([0, 1], size=n, p=[0.4, 0.6])
    print(f"OverTime mean     : {original_overtime:.2f} → {drifted['OverTime'].mean():.2f}")

    # ── Drift 2: JobSatisfaction ───────────────────────────────────
    # Originally spread across 1-4. Now skewed lower — morale dropped
    original_js = drifted["JobSatisfaction"].mean()
    drifted["JobSatisfaction"] = np.random.choice([1, 2, 3, 4], size=n, p=[0.4, 0.35, 0.15, 0.1])
    print(f"JobSatisfaction   : {original_js:.2f} → {drifted['JobSatisfaction'].mean():.2f}")

    # ── Drift 3: MonthlyIncome ─────────────────────────────────────
    # Shift income distribution lower — hiring freeze, lower bands
    original_income = drifted["MonthlyIncome"].mean()
    drifted["MonthlyIncome"] = (drifted["MonthlyIncome"] * 0.75).astype(int)
    print(f"MonthlyIncome mean: {original_income:.0f} → {drifted['MonthlyIncome'].mean():.0f}")

    # ── Drift 4: WorkLifeBalance ───────────────────────────────────
    # Skewed lower — more people reporting poor work life balance
    original_wlb = drifted["WorkLifeBalance"].mean()
    drifted["WorkLifeBalance"] = np.random.choice([1, 2, 3, 4], size=n, p=[0.35, 0.35, 0.2, 0.1])
    print(f"WorkLifeBalance   : {original_wlb:.2f} → {drifted['WorkLifeBalance'].mean():.2f}")

    drifted.to_csv(output_path, index=False)
    print(f"\nDrifted dataset saved: {output_path}")
    print(f"Shape: {drifted.shape}")

    return drifted


if __name__ == "__main__":
    simulate_drift(
        input_path  = "data/processed/X_train.csv",
        output_path = "data/processed/X_drifted.csv"
    )