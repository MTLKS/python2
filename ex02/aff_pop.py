import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from load_csv import load


def convert_population_to_int(df):
    """Converts a string like '1.234B' to 1234000000."""
    if df.endswith("B"):
        return float(df[:-1]) * 1000000000
    elif df.endswith("M"):
        return float(df[:-1]) * 1000000
    elif df.endswith("k"):
        return float(df[:-1]) * 1000
    else:
        return float(df)


def format_tick_with_units(value, pos):
    """Formats a tick with a number and a unit."""
    if abs(value) >= 1e9:
        return f'{value / 1e9:.1f}B'
    elif abs(value) >= 1e6:
        return f'{value / 1e6:.0f}M'
    elif abs(value) >= 1e3:
        return f'{value / 1e3:.0f}K'
    else:
        return str(int(value))


def main():
    """Main function"""
    countries = ["Malaysia", "Singapore"]
    colors = ["tab:green", "tab:blue"]

    df = load("population_total.csv")
    if df is None:
        return

    df = df.transpose()
    results = [df[country].apply(convert_population_to_int)[0:251]
               for country in countries]

    for idx, result in enumerate(results):
        plt.plot(result, color=colors[idx])

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(np.arange(0, 251, 40))
    plt.legend(countries, loc="lower right")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_tick_with_units))
    plt.title("Population Projections")

    plt.savefig("result.png")


if __name__ == "__main__":
    main()
