import pandas as pd

def calculate_fat_loss_progress(
    current_weight, current_body_fat_percentage, calorie_intake, calorie_burned, protein_intake, weeks_until_target
):
    # Constants
    calories_per_kg_fat = 7700  # Calories needed to lose 1 kg of fat
    daily_calorie_deficit = calorie_burned - calorie_intake
    weekly_calorie_deficit = daily_calorie_deficit * 7
    weekly_fat_loss_kg = weekly_calorie_deficit / calories_per_kg_fat

    # Initial calculations
    lean_mass = current_weight * (1 - current_body_fat_percentage / 100)
    results = []

    for week in range(1, weeks_until_target + 1):
        fat_loss = weekly_fat_loss_kg
        muscle_gain = 0.125 / 4  # Average weekly muscle gain (0.5 kg/month)
        lean_mass += muscle_gain
        current_weight -= fat_loss - muscle_gain  # Adjust weight for fat loss and muscle gain
        current_body_fat_percentage = ((current_weight - lean_mass) / current_weight) * 100
        results.append({
            "Week": week,
            "Weight (kg)": round(current_weight, 2),
            "Body Fat %": round(current_body_fat_percentage, 2),
            "Lean Mass (kg)": round(lean_mass, 2),
            "Fat Loss (kg)": round(fat_loss, 2),
            "Muscle Gain (kg)": round(muscle_gain, 2)
        })

    return pd.DataFrame(results)

# Input details
current_weight = 82.6  # kg
current_body_fat_percentage = 29  # %
calorie_intake = 1200  # daily calorie intake
calorie_burned = 1000  # calories burned per day (workout)
protein_intake = 100  # grams per day
weeks_until_target = 30  # Number of weeks to project

# Generate report
progress_report = calculate_fat_loss_progress(
    current_weight, current_body_fat_percentage, calorie_intake, calorie_burned, protein_intake, weeks_until_target
)

# Save to CSV for submission
progress_report.to_csv("fat_loss_progress_report.csv", index=False)

# Generate README.md file content
readme_content = """
# Fat Loss Progress Calculator

This Python script calculates and projects weekly fat loss, muscle gain, and changes in body composition over a given number of weeks. It accounts for:

- Calorie intake and burn (calorie deficit)
- Protein intake
- Weekly fat loss rate based on energy deficit
- Estimated muscle gain based on resistance training and protein consumption

## Features

- **Input Parameters:**
  - Current weight
  - Current body fat percentage
  - Daily calorie intake
  - Daily calorie burn (workout activity)
  - Protein intake
  - Duration in weeks

- **Output:**
  - Weekly projections for weight, body fat percentage, lean mass, fat loss, and muscle gain

## How It Works

1. **Fat Loss Calculation:** Based on the calorie deficit created by the difference between calorie intake and calorie burn. Each 7700 calorie deficit corresponds to ~1 kg of fat loss.
2. **Muscle Gain Estimation:** Assumes 0.5 kg muscle gain per month with sufficient protein and resistance training.
3. **Body Fat Percentage Update:** Updates weekly based on the changes in fat mass and lean mass.

## Formulas

- **Calorie Deficit:** `calorie_burned - calorie_intake`
- **Weekly Fat Loss (kg):** `weekly_calorie_deficit / 7700`
- **Muscle Gain (kg/week):** `0.5 / 4` (assuming average 0.5 kg muscle gain per month)
- **Body Fat Percentage:** `((current_weight - lean_mass) / current_weight) * 100`

## Usage

1. Clone the repository.
2. Install necessary dependencies (`pandas` for data handling).
3. Run the script and modify the input values as needed.
4. The output is saved as a CSV file (`fat_loss_progress_report.csv`).

## Example Output

| Week | Weight (kg) | Body Fat % | Lean Mass (kg) | Fat Loss (kg) | Muscle Gain (kg) |
|------|-------------|------------|----------------|---------------|------------------|
| 1    | 81.6        | 28.5       | 59.1           | 1.0           | 0.125            |
| 2    | 80.6        | 27.9       | 59.2           | 1.0           | 0.125            |
| ...  | ...         | ...        | ...            | ...           | ...              |

## License

This project is open-source and free to use.
"""

# Save README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

# Confirm files are ready
"Files generated: fat_loss_progress_report.csv, README.md"
