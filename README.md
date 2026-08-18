# Thesis-Data-Assessment-01-Prarthana-Nataraj-Subash-
# Data-Driven Analysis of Menstrual Cycle Patterns

## Overview

This project investigates menstrual cycle variability using a longitudinal, cycle-level menstrual health dataset. The study applies exploratory data analysis, correlation analysis, and unsupervised clustering techniques to identify and characterize recurring menstrual cycle patterns.

The analysis focuses on understanding how cycle-level indicators such as cycle length, estimated ovulation day, luteal phase length, menses duration, and total menses score vary and interact across repeated menstrual cycles.

The identified groups are interpreted as **exploratory data-derived cycle profiles**, rather than clinically distinct or diagnostic categories.

---

## Research Objective

The main objective of this study is:

> **To investigate menstrual cycle variability using data-driven analytical and clustering techniques and to identify recurring patterns within longitudinal cycle-level data.**

The study aims to:

- Explore the distribution of menstrual cycle characteristics.
- Examine relationships between cycle-level variables.
- Identify recurring cycle-pattern groups using clustering.
- Compare different clustering approaches.
- Investigate whether identified cycle profiles persist across repeated cycles.
- Discuss the potential relevance of these findings for future digital health applications.

---

## Dataset

The study uses a publicly available menstrual cycle dataset obtained from Kaggle and originally derived from research conducted by Fehring and made available through Marquette University.

The dataset contains approximately:

- **1,665 cycle-level observations**
- **80 variables**
- Multiple observations from individual participants

The dataset is longitudinal, meaning that several participants contribute observations from multiple menstrual cycles.

### Important Dataset Characteristics

The dataset primarily contains cycle-tracking and menstrual-health indicators rather than a complete demographic or lifestyle profile.

Several demographic and physiological variables contain substantial missing data. Therefore, variables with insufficient completeness were excluded from the primary clustering analysis.

---

## Variables Used for Clustering

The final clustering analysis was based on five consistently recorded numerical cycle-level indicators:

| Variable | Description |
|---|---|
| `LengthofCycle` | Length of the menstrual cycle in days |
| `EstimatedDayofOvulation` | Estimated day of ovulation |
| `LengthofLutealPhase` | Length of the luteal phase |
| `LengthofMenses` | Duration of menstrual bleeding |
| `TotalMensesScore` | Total menses-related score |

These variables were selected based on their relevance to menstrual cycle characterization and their availability after data-quality assessment.

---

## Data Preprocessing

The preprocessing workflow included:

1. Inspecting important variables and their value distributions.
2. Identifying blank entries and converting them to missing values.
3. Quantifying missing values for all variables.
4. Calculating missing-value percentages.
5. Assessing missingness in selected variables.
6. Selecting consistently recorded cycle-level variables.
7. Removing observations with missing values in the variables required for clustering.
8. Standardizing the selected numerical variables before clustering.

After preprocessing, **1,512 observations** were available for the clustering analysis.

---

## Exploratory Data Analysis

Exploratory data analysis was performed to understand the distributions and characteristics of the selected menstrual cycle variables.

The analysis included:

- Histograms
- Boxplots
- Descriptive statistics
- Distribution analysis
- Outlier inspection
- Correlation analysis

### Main Observations

Cycle length was primarily concentrated around the mid-to-high 20-day range, while menses duration was generally concentrated around approximately 4–6 days.

The distributions also contained some extreme observations, particularly for variables such as luteal phase length and menses-related measurements.

---

## Correlation Analysis

Pearson correlation analysis was performed to examine relationships between the five selected variables.

Important relationships included:

- `LengthofCycle` and `EstimatedDayofOvulation`: **r = 0.737**
- `LengthofMenses` and `TotalMensesScore`: **r = 0.829**
- `LengthofCycle` and `LengthofLutealPhase`: **r = 0.415**
- `EstimatedDayofOvulation` and `LengthofLutealPhase`: **r = -0.286**

The strongest relationship was observed between menses duration and total menses score.

These results indicate that some menstrual characteristics are strongly associated, while other variables provide additional information about cycle structure.

---

# Clustering Analysis

## K-Means Clustering

K-Means clustering was applied to the standardized five-variable dataset.

Several values of K were evaluated using the Elbow Method and Silhouette Analysis.

### Cluster Selection

Silhouette scores were evaluated for K values from 2 to 10.

The highest Silhouette Score was obtained for:

**K = 4 → Silhouette Score = 0.286**

Considering the Elbow Method together with Silhouette Analysis, four clusters were selected for the subsequent K-Means analysis.

The relatively low Silhouette Score indicates that the resulting groups have some overlap. Therefore, the clusters are interpreted as exploratory cycle-pattern profiles rather than strictly separated categories.

---

## K-Means Cluster Profiles

Four exploratory profiles were identified.

| Cluster | Cycle Length | Ovulation Day | Luteal Phase | Menses Length | Menses Score |
|---|---:|---:|---:|---:|---:|
| 0 | 27.35 | 14.17 | 13.16 | 4.47 | 8.27 |
| 1 | 28.31 | 15.98 | 12.29 | 6.55 | 12.68 |
| 2 | 34.16 | 14.19 | 20.05 | 5.86 | 11.15 |
| 3 | 34.15 | 21.27 | 12.92 | 5.25 | 9.66 |

### Profile Interpretation

**Cluster 0**
- Shorter average cycle length
- Earlier estimated ovulation
- Shorter menses duration
- Lowest average menses score

**Cluster 1**
- Shorter average cycle length
- Longer menses duration
- Highest average menses score

**Cluster 2**
- Longer average cycle length
- Similar ovulation timing to Cluster 0
- Notably extended luteal phase

**Cluster 3**
- Longer average cycle length
- Latest estimated ovulation
- Luteal phase similar to Clusters 0 and 1

These profiles represent recurring combinations of cycle characteristics rather than clinical classifications.

---

# Hierarchical Clustering

Hierarchical clustering was performed as a complementary unsupervised clustering approach.

The resulting groups showed different distributions compared with K-Means, although several broad cycle characteristics were also observable.

### Hierarchical Cluster Profiles

| Cluster | Cycle Length | Ovulation Day | Luteal Phase | Menses Length | Menses Score |
|---|---:|---:|---:|---:|---:|
| 0 | 34.00 | 20.69 | 13.35 | 5.98 | 11.51 |
| 1 | 31.59 | 14.73 | 16.91 | 5.48 | 10.26 |
| 2 | 27.64 | 14.67 | 12.95 | 3.96 | 7.16 |
| 3 | 27.18 | 14.92 | 12.22 | 5.70 | 10.79 |

The hierarchical clustering results provide a complementary perspective on the structure present in the data.

---

# Comparison of Clustering Methods

The K-Means and hierarchical clustering assignments were compared using the Adjusted Rand Index (ARI).

### Adjusted Rand Index

**ARI = 0.277**

This indicates modest agreement between the two clustering approaches.

The difference between the clustering assignments suggests that the exact grouping of observations depends partly on the clustering method used.

Together with the relatively low Silhouette Score, this supports cautious interpretation of the identified profiles.

---

# Longitudinal Analysis

Because the dataset contains repeated cycles from individual participants, a longitudinal analysis was performed to investigate whether cluster profiles persist across consecutive cycles.

The analysis included:

- **1,512 observations**
- **157 unique participants**
- Approximately **9.63 cycles per participant on average**
- **1,355 consecutive cycle transitions**

### Cluster Persistence

Among the 1,355 consecutive cycle transitions:

- **874 transitions (64.50%)** remained in the same cluster.
- **481 transitions (35.50%)** changed to another cluster.

This indicates that the identified cycle profiles show a degree of persistence across repeated cycles while also demonstrating substantial cycle-to-cycle variability.

---

## Cluster Transition Analysis

A transition matrix was created to examine how cycles moved between profiles.

The main patterns showed:

- Strong persistence within Clusters 0 and 1.
- Additional persistence within Cluster 3.
- Profile changes occurring particularly among Clusters 0, 1, and 3.
- Fewer transitions involving Cluster 2, consistent with its smaller K-Means cluster size.

Overall, the transition analysis suggests that menstrual cycle profiles are neither completely fixed nor completely random across repeated observations.

---

# Key Findings

The main findings of the analysis are:

1. Menstrual cycle characteristics show substantial variation across observations.
2. Several cycle-level variables demonstrate meaningful correlations.
3. Four exploratory cycle-pattern profiles were identified using K-Means clustering.
4. The clusters show some overlap, as indicated by the relatively low Silhouette Score of **0.286**.
5. Hierarchical clustering produced a complementary but not identical grouping structure.
6. The Adjusted Rand Index of **0.277** indicates modest agreement between the two clustering approaches.
7. Longitudinal analysis showed that **64.50% of consecutive cycle transitions remained within the same profile**.
8. Approximately **35.50% of transitions changed profile**, demonstrating cycle-to-cycle variability.
9. The findings suggest that menstrual cycle characteristics can form recurring but overlapping patterns across repeated observations.

---

# Research Significance

The contribution of this study is not simply the identification of clusters.

Instead, the study provides a data-driven characterization of menstrual cycle variability by combining:

- Exploratory analysis
- Variable relationships
- Unsupervised pattern discovery
- Comparison of clustering approaches
- Longitudinal profile analysis

This approach provides a structured way to investigate recurring menstrual cycle characteristics within longitudinal data.

---

# Digital Health Relevance

The identified cycle-pattern profiles may provide a conceptual basis for future digital health systems focused on menstrual health.

Potential applications could include:

- Personalized cycle visualization
- Longitudinal cycle monitoring
- Identification of changes from an individual's usual pattern
- Data-driven cycle summaries
- Non-diagnostic menstrual health insights

The current study does **not** develop or validate a medical diagnostic system. The identified clusters should therefore not be interpreted as clinical diagnoses or medical risk categories.

---

# Limitations

Several limitations should be considered:

- Significant missingness in demographic and physiological variables.
- The dataset primarily represents cycle-level tracking information rather than a comprehensive health profile.
- The dataset represents a specific study population and may not generalize to the wider population.
- The clustering profiles show substantial overlap.
- The Silhouette Score indicates relatively weak cluster separation.
- The modest ARI indicates differences between clustering approaches.
- The analysis identifies associations and patterns but does not establish causal relationships.
- The smaller size of some clusters may affect the stability and interpretation of their profiles.

---

# Tools and Technologies

The project uses:

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **Jupyter Notebook**

Main analytical methods include:

- Data cleaning
- Missing-value analysis
- Exploratory Data Analysis
- Correlation analysis
- Feature selection
- Standardization
- K-Means clustering
- Silhouette analysis
- Elbow Method
- Hierarchical clustering
- Adjusted Rand Index
- Longitudinal cluster transition analysis

---

# Project Structure

```text
├── Data Quality Assessment.ipynb
├── README.md
└── data/
    └── [dataset files]
