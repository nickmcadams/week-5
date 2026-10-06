import plotly.express as px
import pandas as pd

def survival_demographics():
    """Summarize Titanic survival by class, sex, and age group."""

    df = pd.read_csv(
        "https://raw.githubusercontent.com/"
        "datasciencedojo/datasets/master/titanic.csv"
    )

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 12, 19, 59, float("inf")],
        labels=["Child", "Teen", "Adult", "Senior"],
        include_lowest=True
    )

    results = (
        df.groupby(
            ["pclass", "sex", "age_group"],
            observed=False
        )
        .agg(
            n_passengers=("passengerid", "count"),
            n_survivors=("survived", "sum")
        )
        .reset_index()
    )

    results["survival_rate"] = (
        results["n_survivors"] / results["n_passengers"]
    )

    results = results.sort_values(
        ["pclass", "sex", "age_group"]
    ).reset_index(drop=True)

    return results


def visualize_demographic():
    """Visualize Titanic survival rates by class, sex, and age group."""

    df = survival_demographics()

    fig = px.bar(
        df,
        x="age_group",
        y="survival_rate",
        color="sex",
        facet_col="pclass",
        barmode="group",
        labels={
            "age_group": "Age Group",
            "survival_rate": "Survival Rate",
            "sex": "Sex",
            "pclass": "Passenger Class"
        },
        title="Titanic Survival Rates by Class, Sex, and Age Group"
    )

    return fig

def family_groups():
    """Summarize Titanic fares by family size and passenger class."""

    df = pd.read_csv(
        "https://raw.githubusercontent.com/"
        "datasciencedojo/datasets/master/titanic.csv"
    )

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df["family_size"] = df["sibsp"] + df["parch"] + 1

    results = (
        df.groupby(
            ["pclass", "family_size"]
        )
        .agg(
            n_passengers=("passengerid", "count"),
            avg_fare=("fare", "mean"),
            min_fare=("fare", "min"),
            max_fare=("fare", "max")
        )
        .reset_index()
        .sort_values(
            ["pclass", "family_size"]
        )
        .reset_index(drop=True)
    )

    return results

def last_names():
    """Return counts of Titanic passenger last names."""

    df = pd.read_csv(
        "https://raw.githubusercontent.com/"
        "datasciencedojo/datasets/master/titanic.csv"
    )

    last_names = (
        df["Name"]
        .str.split(",")
        .str[0]
        .str.strip()
    )

    return last_names.value_counts()

def visualize_families():
    """Visualize average fare by family size and passenger class."""

    df = family_groups()

    fig = px.line(
        df,
        x="family_size",
        y="avg_fare",
        color="pclass",
        markers=True,
        labels={
            "family_size": "Family Size",
            "avg_fare": "Average Fare",
            "pclass": "Passenger Class"
        },
        title="Average Titanic Fare by Family Size and Passenger Class"
    )

    return fig
