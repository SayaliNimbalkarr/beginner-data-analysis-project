Summary
-------
This PR implements the enhancements described in Issue #1:
- Standardize column names and full data cleaning for Project 1 - Weather.
- Added EDA: correlation heatmap, time-series plots, boxplots, monthly aggregation.
- Implemented a simple next-hour temperature prediction using LinearRegression (scikit-learn). Includes model evaluation (MAE, R²).
- Exported cleaned dataset `clean_weather_with_predictions.csv` for dashboarding.
- Updated README with usage instructions and screenshots.

Files changed
-------------
- Project 1 - Weather/project 1 - weather.ipynb  (cleaning, EDA, model)
- weather_predictions.csv
- README.md (updated instructions & screenshots)
- (optional) PowerBI/WeatherDashboard.pbix

How to run
----------
1. Open the notebook `Project 1 - Weather/project 1 - weather.ipynb`.
2. Ensure dependencies: `pip install -r requirements.txt` (or scikit-learn, pandas, matplotlib, seaborn).
3. To export CSV: run the final cell that writes `clean_weather_with_predictions.csv`.

Notes
-----
We already discussed this plan with @punneko and received approval to contribute (original message: "I am interested in contributing..."). Please let us know if you'd like changes or prefer a different model or UI (Tkinter/Streamlit).
