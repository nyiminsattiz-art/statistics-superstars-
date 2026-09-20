# Final Report: Statistical Analysis of the Iris Dataset

## Team: Statistics Superstars
**Date:** September 20, 2026

---

## 1. Project Overview

Over four weeks, our team conducted a complete statistical analysis workflow on the Iris dataset -- from data acquisition and cleaning, through hypothesis testing and distribution analysis, to building an interactive dashboard for exploring our findings. This report summarizes the full project.

**Team Members:**
- Student A (Nyi Min Satt) -- Project Lead & Data Curator
- Student B (Lappawat Mahawong) -- Statistical Analyst
- Student C (Zongting Li) -- Visualization Specialist

**Repository:** https://github.com/nyiminsattiz-art/statistics-superstars-

---

## 2. Dataset

**Selected Dataset:** Iris

**Source:** UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/53/iris), loaded via scikit-learn's `load_iris()`.

**Description:** 150 measurements of iris flowers across three species (setosa, versicolor, virginica), with four physical measurements (sepal length, sepal width, petal length, petal width) plus species label. Two derived columns (sepal_area, petal_area) were added during cleaning.

**Final Shape:** 149 rows x 7 columns (after removing 1 duplicate)

---

## 3. Data Cleaning (Week 1)

- Checked for missing values -- found none
- Removed 1 duplicate row
- Converted `species` to categorical type
- Detected and capped 4 outliers in sepal width using the IQR method, to the range [2.05, 4.05]
- Added derived columns: `sepal_area` and `petal_area` (length x width)

See `reports/cleaning_log.txt` for full details.

---

## 4. Statistical Analysis (Week 2)

### 4.1 Hypothesis Testing

| Test | Variables | Statistic | p-value | Significant |
|------|-----------|-----------|---------|-------------|
| One-sample t-test | sepal length (cm) vs 5.5 | t = 5.048 | 1.29e-06 | Yes |
| Independent t-test | petal length: setosa vs versicolor | t = -39.493 | 5.40e-62 | Yes |
| One-way ANOVA | petal length by species | F = 1176.84 | 8.96e-91 | Yes |

**Key finding:** Petal length differs extremely significantly between species -- this is one of the strongest signals in the entire dataset.

### 4.2 Distribution Fitting

| Variable | Best Fit | p-value | Good Fit? |
|----------|----------|---------|-----------|
| sepal length (cm) | Gamma | 0.248 | Yes |
| sepal width (cm) | Gamma | 0.175 | Yes |
| petal length (cm) | Gamma | 1.41e-05 | No |
| petal width (cm) | Gamma | 0.0002 | No |
| sepal_area | Gamma | 0.910 | Yes |
| petal_area | Gamma | 7.34e-06 | No |

**Key finding:** Sepal-related measurements fit a Gamma distribution well; petal-related measurements do not fit any standard distribution well, likely because petal size varies so dramatically between species that the combined data doesn't follow one smooth shape.

### 4.3 Confidence Intervals

We calculated 95% confidence intervals using two methods -- traditional (based on the t/z distribution) and bootstrap (10,000 resamples). Both methods produced nearly identical intervals across all variables (differences under 0.02 in width), confirming our sample size is large enough for the traditional method to be reliable.

Example: petal length -- 95% CI of (3.47, 4.03) cm using both methods.

---

## 5. Visualization & Dashboard (Week 3)

We built an interactive Streamlit dashboard (`dashboard/app.py`) allowing users to:
- Filter data by species using a sidebar multi-select
- Explore relationships between any two numeric variables via an interactive scatter plot
- Compare measurement distributions across species using box plots
- View a correlation heatmap of all numeric variables
- Browse the underlying filtered data in a table

The dashboard uses Plotly for interactivity and caches data loading for performance. Static exploratory visualizations (histograms, box plots, correlation heatmap, 3D scatter, Q-Q plots) were also created earlier in `notebooks/03_exploratory_visualizations.ipynb`.

We also wrote 8 automated unit tests (`tests/test_data_loader.py`) verifying our data loading and cleaning pipeline behaves correctly -- all passing.

---

## 6. Overall Conclusions

1. **Petal measurements are the strongest predictor of species.** Petal length and petal width differ dramatically and significantly between species, while sepal measurements overlap more and show weaker separation.

2. **Petal measurements are highly correlated with each other** (petal length, petal width, and petal_area all correlate above 0.95), suggesting they largely carry redundant information -- a single petal measurement could likely serve as a strong proxy for identifying species.

3. **Most variables are not normally distributed**, which informed our choice of statistical methods throughout (e.g., relying on ANOVA and bootstrap methods rather than assuming normality everywhere).

4. **Sample size was sufficient for reliable inference** -- our traditional and bootstrap confidence intervals matched closely, giving confidence in our statistical conclusions despite non-normality in several variables.

---

## 7. Limitations

- The dataset is limited to 149 flowers across only 3 species -- findings are specific to Iris flowers and may not generalize.
- Several variables failed normality tests, meaning some statistical assumptions were violated; we addressed this by cross-checking with bootstrap methods and non-parametric approaches where appropriate.
- No external validation dataset was used to confirm findings beyond the original sample.

---

## 8. Team Contributions (Full Project)

| Team Member | Key Contributions |
|-------------|--------------------|
| Student A (Nyi Min Satt) | GitHub repository setup, project structure, data cleaning, environment management, unit tests, all three weekly reports, team coordination |
| Student B (Lappawat Mahawong) | Statistics module (StatisticalAnalyzer class), hypothesis testing, distribution fitting, confidence intervals & bootstrap, code review |
| Student C (Zongting Li) | Exploratory visualizations, interactive Streamlit dashboard |

---

## Appendix

**Repository Structure:**
- `data/` -- raw and processed datasets
- `notebooks/` -- all analysis notebooks (inspection, cleaning, hypothesis testing, distribution fitting, confidence intervals, visualizations)
- `src/` -- reusable code (DataLoader, StatisticalAnalyzer)
- `dashboard/` -- interactive Streamlit application
- `tests/` -- automated unit tests
- `reports/` -- weekly reports, summary statistics, and figures

**Weekly Reports:**
- `reports/week1_report.md`
- `reports/week2_report.md`
- `reports/final_report.md` (this document)

**Live Dashboard:** Run with `streamlit run dashboard/app.py`
