# Hypothesis Testing
##  ANOVA & Kruskal–Wallis (Digital Services Subscription)

This project analyzes a digital services subscription dataset using:

* **One-way ANOVA** (parametric) 
* **Kruskal–Wallis** (nonparametric) 

The goal is to compare groups (based on a categorical feature) to determine whether there are statistically significant differences in a numeric outcome.

## Project Structure

```
.
├── data/
│   └── subscription_dataset.csv
├── docs/
│   └── Digital Services Subscription Data Dictionary.docx
├── notebooks/
│   ├── 01_anova.ipynb
│   └── 02_kruskal_wallis.ipynb
├── reports/
│   ├── anova.html
│   └── kruskal_wallis.html
└── src/
    ├── anova.py
    └── kruskal_wallis.py
```

## Requirements

These are inferred directly from the current script imports:

* Python 3.x
* `pandas`
* `matplotlib`
* `seaborn`
* `scipy`

Install:

```bash
pip install pandas matplotlib seaborn scipy
```

## How to Run

### Run scripts

From inside `src/` (recommended, because `DATA_PATH` is `../data/subscription_dataset.csv`):

```bash
cd src
python anova.py
python kruskal_wallis.py
```

If you run from the project root, the relative path likely won’t resolve (unless you change `DATA_PATH` or handle paths dynamically).

### Run notebooks

Open and run:

* `notebooks/01_anova.ipynb`
* `notebooks/02_kruskal_wallis.ipynb`

HTML exports are available in `reports/`:

* `reports/anova.html`
* `reports/kruskal_wallis.html`

## Data

* `data/subscription_dataset.csv` is the dataset used by both analyses.
* `docs/Digital Services Subscription Data Dictionary.docx` describes fields, valid values, and business meaning.

## What the Scripts Do

Both `src/anova.py` and `src/kruskal_wallis.py` currently:

* load the CSV from `../data/subscription_dataset.csv`
* use helper functions like `print_section()` to output readable console sections
* include visualization libraries (`matplotlib`, `seaborn`) suggesting they generate plots as part of the analysis workflow

The ANOVA script imports `f_oneway` directly:

```python
from scipy.stats import f_oneway
```

The Kruskal–Wallis script imports SciPy stats as a module:

```python
from scipy import stats
```


