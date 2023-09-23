import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def main():
    """Main function"""
    country = "Malaysia"

    df = load("life_expectancy_years.csv")
    if df is None:
        return

    df = df.transpose()
    result = df[country]

    plt.plot(result)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(np.arange(0, 300, 40))
    plt.title(f"{country} Life expectancy Projections")

    plt.savefig("result.png")


if __name__ == "__main__":
    main()
