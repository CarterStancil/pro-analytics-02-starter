# NBA Tracking Data Analysis (2024–2025 Season)

## Project Overview
This project analyzes **NBA player tracking drives data** from the 2024–25 season to explore how player roles and playstyles influence team success.  
By segmenting players into three tiers — **Superstars**, **Secondary Stars**, and **Role Players** — this analysis examines how key performance metrics differ between **wins** and **losses**, and what factors most strongly drive **scoring efficiency** and **team outcomes**.

The project progresses through data cleaning, exploration, segmentation, statistical testing, and predictive modeling to uncover actionable insights into modern basketball analytics.

## Objectives 
- Do NBA players tend to record more drives in games that result in wins compared to losses? 
- Does the role of certain players affect the number of drives? 
- Is there a consistent relationship between the number of drives and the overall success rate of a team?
- Does superstars' drive rate have a greater effect on a team's success than rising stars or role players? 

---

## Repository Structure

NBA_Drives_Analysis/
│
├── NBATrackingDataWins24-25.csv
├── NBATrackingDataLosses24-25.csv
├── NBATrackingDataWins24-25_clean.csv
├── NBATrackingDataLosses24-25_clean.csv
├── NBATrackingDataWins24-25_per36.csv
├── NBATrackingDataLosses24-25_per36.csv
│
├── 01_Initial_Exploration.ipynb
├── 02_Exploratory_Data_Analysis.ipynb
├── 03_Segmented_Performance_Analysis.ipynb
├── 04_Linear_Regression_Analysis.ipynb
├── 05_Predictive_Modeling.ipynb
│
└── README.md

---

## Data Preparation
- **clean_data.py** is ran to remove players who don't appear on both data sets. This ensures that only players with winning and losing outcomes are included
- Raw player tracking data for **wins** and **losses** was cleaned to handle missing values and standardize columns.  
- A **Per-36 normalization** was applied to control for differences in playing time.  
- Players were segmented into **three tiers** based on scoring averages and team role.

---

## Initial Observations

A preliminary review of the data revealed early trends distinguishing wins from losses:

- **Scoring volume (FGM)** was higher in *losses*, suggesting that raw output doesn’t guarantee wins.  
- **Assists** were notably higher in *wins*, emphasizing ball movement and playmaking as key to success.  
- **Free Throws (FTM, FTA)** were higher in *losses*, implying reliance on foul-drawing when behind.  
- **Drives** showed strong distribution differences, marking them as a potential driver of outcome and later analysis focus.

These early insights informed the subsequent statistical and predictive modeling phases.

---

## Statistical Analysis

### **ANOVA Results**
All main metrics showed **statistically significant differences (p < 0.05)** across tiers for both wins and losses, indicating that at least one player tier performed meaningfully differently in each category.

| Metric | Wins (F, p) | Losses (F, p) | Interpretation |
|:-------|:-------------|:--------------|:----------------|
| **DRIVES_Per36** | F = 34.45, p = 0.0000 | F = 32.08, p = 0.0000 | Driving frequency differs significantly among tiers; superstars drive more overall. |
| **PTS_Per36** | F = 66.83, p = 0.0000 | F = 53.44, p = 0.0000 | Strong tier differences in scoring efficiency and usage. |
| **FGA_Per36** | F = 41.24, p = 0.0000 | F = 33.62, p = 0.0000 | Shooting volume is tier-dependent, highest for superstars. |
| **AST_Per36** | F = 20.85, p = 0.0000 | F = 3.53, p = 0.0301 | Playmaking differs significantly, especially in wins. |
| **PASS_Per36** | F = 11.40, p = 0.0000 | F = 10.93, p = 0.0000 | Passing behavior varies by tier. |
| **TO_Per36** | F = 3.71, p = 0.0251 | F = 7.64, p = 0.0005 | Turnover rates differ modestly by tier. |
| **FTA_Per36** | F = 44.56, p = 0.0000 | F = 49.59, p = 0.0000 | Free-throw attempts vary substantially among tiers. |
| **PF_Per36** | F = 44.23, p = 0.0000 | F = 48.76, p = 0.0000 | Foul rates also show clear differences across tiers. |

---

### **Tukey HSD Results (Directional Mean Differences)**

Post-hoc Tukey HSD comparisons revealed **where** and **how** player performance differs:

- The strongest mean differences appear between **Role Players and Superstars**, and **Role Players and Secondary Stars**, especially for *Drives*, *PTS*, and *FGA*.  
- **Superstars** consistently post higher *Drives* (+5–6), *PTS* (+4–5), and *FGA* (+2–3), confirming dominant offensive roles.  
- **Secondary Stars** exhibit smaller but consistent increases over Role Players, reflecting balanced scoring and playmaking roles.  
- **Secondary Star vs. Superstar** comparisons show minimal differences, suggesting similar per-36 output levels despite differing team dependence.

Heatmaps of directional differences show warm tones favoring higher tiers, underscoring the offensive gap between stars and supporting players.

---

### **Interpretation – Per-36 Stat Differences (Wins vs. Losses)**

Tier-specific trends reveal performance behaviors linked to team success:

- **Superstars:**  
  - Larger negative differences in *Drives*, *FGA*, and *PTS* during wins.  
  - Teams win when superstars **don’t need to dominate offensively**, indicating balance and support effectiveness.  
  - In losses, higher isolation and usage suggest overreliance.

- **Secondary Stars:**  
  - Noticeable **increases in assists and passes** during wins.  
  - Suggests that when secondary stars facilitate more, team synergy improves.

- **Role Players:**  
  - Relatively **stable output** across wins and losses.  
  - Reflects consistent complementary contributions regardless of result.

**Overall takeaway:**  
Winning teams display **balanced offensive distribution and ball movement**, while losing efforts often involve **superstars shouldering excess load**.

---

## Predictive Modeling

### Objective
Predict **player scoring output (PTS_Per36)** and identify **key performance drivers** using Random Forest and XGBoost regression models for each tier and outcome (Wins / Losses).

### Model Performance Summary

| Tier | Outcome | Model | R² | RMSE |
|:------|:---------|:--------|:----:|:----:|
| Superstar | Wins | Random Forest | 0.479 | 1.414 |
| Superstar | Wins | XGBoost | 0.645 | 1.167 |
| Superstar | Losses | Random Forest | 0.318 | 2.059 |
| Superstar | Losses | XGBoost | 0.143 | 2.308 |
| Secondary Star | Wins | Random Forest | 0.877 | 0.865 |
| Secondary Star | Wins | XGBoost | 0.877 | 0.867 |
| Secondary Star | Losses | Random Forest | 0.808 | 1.150 |
| Secondary Star | Losses | XGBoost | 0.789 | 1.206 |
| Role Player | Wins | Random Forest | 0.762 | 1.157 |
| Role Player | Wins | XGBoost | 0.812 | 1.029 |
| Role Player | Losses | Random Forest | 0.614 | 1.428 |
| Role Player | Losses | XGBoost | 0.625 | 1.407 |

### Interpretation
- **XGBoost** generally outperformed Random Forest for **Superstars and Role Players**, indicating it captures complex nonlinear relationships slightly better.  
- **Secondary Stars** achieved the **highest predictive accuracy** (R² ≈ 0.88), suggesting their scoring patterns are most consistent and predictable.  
- **Superstars** showed lower predictability, especially in losses — reflecting high variability in offensive role depending on game context.  
- **Role Players** demonstrated solid predictability (R² ≈ 0.76–0.81), likely due to consistent, limited offensive duties.

These results highlight that **scoring variability increases with player responsibility**: the more central a player is to team offense, the less stable their output becomes.

---

## Key Insights & Takeaways

- Team success correlates more strongly with **assists, passes, and balance** than with pure scoring volume.  
- **Superstars win** when usage decreases slightly and teammates contribute more offensively.  
- **Secondary Stars** thrive as facilitators, linking scoring and playmaking.  
- **Role Players** maintain steady output independent of result, emphasizing reliability over volume.  
- Predictive models confirm that **consistency and team integration**, rather than isolation scoring, are hallmarks of winning performance.

---

## Next Steps
Future work could include:
- Integrating **game-level data** to model *win probability per performance profile*.  
- Incorporating **positional segmentation** (guards, forwards, centers).  
- Exploring **advanced clustering (K-Means, PCA)** for unsupervised player-type discovery.  

---

## Summary
This project connects traditional basketball analytics with modern machine learning to dissect how **individual behaviors translate to team outcomes**.  
Through descriptive, inferential, and predictive methods, it demonstrates that **winning basketball is collective**, while **losses magnify isolation and overuse**.

---
