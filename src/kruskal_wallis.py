# -----------------------------
# Imports
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

DATA_PATH = "../data/subscription_dataset.csv"

# -----------------------------
# Utilities
# -----------------------------
def die(message, exc=None):
    print(message)
    if exc is not None:
        print(exc)
    raise SystemExit(1)

def print_section(title):
    print(f"=== {title} ===")

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        die('Failed to load dataset.', e)

def data_profile(df):
    dtypes = df.dtypes.astype(str)
    uniq = df.nunique(dropna=True)

    samples = []
    for col in df.columns:
        vals = df[col].dropna().unique()[:5].tolist()
        samples.append(vals)

    summary = pd.DataFrame(
        {
            "dtype": dtypes,
            "unique_values": uniq,
            "example_values": samples,
        }
    )
    print("\nVariable summary (dtype + samples):")
    print(summary.to_string())

def distributions(df):
    # annual_spend_usd - histogram
    sns.histplot(df['annual_spend_usd'])
    plt.xlabel('Annual Spend USD')
    plt.ylabel('Count')
    plt.title('Annual Spend USD Distribution')
    plt.show()

    # market_region - count plot
    plt.clf()
    sns.countplot(x="market_region", data=df)
    plt.xlabel("Market Region")
    plt.ylabel("Count")
    plt.title("Market Region Counts")
    plt.show()

def kruskal_wallis(df):
    coastal_south = df.loc[df["market_region"] == "coastal_south", "annual_spend_usd"].tolist()
    inland_south = df.loc[df["market_region"] == "inland_south", "annual_spend_usd"].tolist()
    inland_north = df.loc[df["market_region"] == "inland_north", "annual_spend_usd"].tolist()
    coastal_north= df.loc[df["market_region"] == "coastal_north", "annual_spend_usd"].tolist()


    result = stats.kruskal(coastal_south, inland_south, inland_north, coastal_north)

    print("One-Way ANOVA (annual spending by market region)")
    print("statistic =", round(result.statistic, 4))
    print("pvalue =", round(result.pvalue, 4))
    print()

def main(): 
    df = load_data(DATA_PATH)

    # Data Profile
    print_section('Data Profile')
    data_profile(df)

    # Distributions
    print_section('Relevant Distributions')
    distributions(df)

    # Kruskal-Wallis test
    print_section('Kruskal-Wallis Test')
    kruskal_wallis(df)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        die('Unexpected error.', e)