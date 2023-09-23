from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Main function"""
    year = "1900"

    tick_locations = [300, 1000, 10000]
    tick_labels = ["300", "1k", "10k"]

    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    if income is None or life is None:
        return

    plt.scatter(income[year], life[year])
    plt.xscale("log")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xticks(tick_locations, tick_labels)
    plt.title(year)
    plt.savefig("result.png")


if __name__ == "__main__":
    main()
