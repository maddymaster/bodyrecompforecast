# bodyrecompforecast
this is a personal script that i m making it public

---

# Fat Loss Progress Calculator

## Overview

The **Fat Loss Progress Calculator** is a Python-based tool designed to project weekly changes in body composition, including weight, body fat percentage, lean mass, fat loss, and muscle gain. This script provides accurate forecasts based on inputs such as calorie intake, calorie burn, and workout routines, helping users plan their fitness journey effectively.

## Features

- **Input Parameters:**
  - Current weight
  - Current body fat percentage
  - Daily calorie intake
  - Daily calorie burn (workouts, cardio, resistance training)
  - Protein intake (grams/day)
  - Duration in weeks for projection

- **Output:**
  - Weekly breakdown of:
    - Weight
    - Body fat percentage
    - Lean mass
    - Fat loss
    - Muscle gain

- **Export Results:** Automatically saves the output as a CSV file for easy analysis and sharing.

## How It Works

### Calculations
1. **Fat Loss:**
   - Based on the calorie deficit created by the difference between calorie intake and calorie burn.
   - Formula:  
     \( \text{Fat Loss (kg)} = \frac{\text{Calorie Deficit}}{7700} \)
   - Each 7,700 kcal deficit corresponds to approximately 1 kg of fat loss.

2. **Muscle Gain:**
   - Estimated based on sufficient protein intake and resistance training.
   - Assumes an average of **0.5 kg muscle gain per month**, adjusted for weekly progress.

3. **Body Fat Percentage:**
   - Updates weekly based on the changes in fat mass and lean mass.
   - Formula:  
     \( \text{Body Fat Percentage} = \left( \frac{\text{Weight} - \text{Lean Mass}}{\text{Weight}} \right) \times 100 \)

4. **Lean Mass:**
   - Calculated by adding weekly muscle gain to the initial lean mass.

## Input Example
To customize your forecast, modify the following variables in the script:

```python
current_weight = 82.6  # Current weight in kg
current_body_fat_percentage = 29  # Current body fat percentage in %
calorie_intake = 1200  # Daily calorie intake
calorie_burned = 1000  # Calories burned daily (exercise + activity)
protein_intake = 100  # Protein intake in grams per day
weeks_until_target = 30  # Number of weeks for projection
```

## Output Example

The script generates a CSV file (`fat_loss_progress_report.csv`) with the following structure:

| Week | Weight (kg) | Body Fat % | Lean Mass (kg) | Fat Loss (kg) | Muscle Gain (kg) |
|------|-------------|------------|----------------|---------------|------------------|
| 1    | 81.6        | 28.5       | 59.1           | 1.0           | 0.125            |
| 2    | 80.6        | 27.9       | 59.2           | 1.0           | 0.125            |
| ...  | ...         | ...        | ...            | ...           | ...              |

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/fat-loss-calculator.git
   cd fat-loss-calculator
   ```

2. **Install Dependencies:**
   This project requires Python and the `pandas` library for data handling. Install pandas using pip:
   ```bash
   pip install pandas
   ```

3. **Run the Script:**
   Modify the input variables in the script (`fat_loss_calculator.py`) and execute it:
   ```bash
   python fat_loss_calculator.py
   ```

4. **View Results:**
   The script generates:
   - `fat_loss_progress_report.csv`: Detailed progress report.
   - `README.md`: Documentation file for the project.

## License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---
You can leave me some stars if you liked this code
