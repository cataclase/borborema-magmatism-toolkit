import matplotlib.pyplot as plt


def plot_upb_ages(df, colors):
    """
    Plot zircon U-Pb ages with analytical uncertainty.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset containing age and uncertainty.

    colors : dict
        Mapping of suites to colors.

    Returns
    -------
    matplotlib.figure.Figure
    """

    fig, ax = plt.subplots(figsize=(10,8))

    df = df.sort_values(by="Age (Ma)", ascending=False)

    df["index"] = range(len(df))

    for _, row in df.iterrows():

        c = colors.get(row["Suite"], "gray")

        ax.errorbar(
            row["Age (Ma)"],
            row["index"],
            xerr=row["Error 2S"],
            fmt="o",
            color=c,
            ecolor=c,
            elinewidth=1.5,
            capsize=4
        )

    ax.set_xlabel("Zircon U–Pb age (Ma)")
    ax.set_ylabel("Pluton")

    ax.invert_xaxis()

    plt.grid(True, linestyle="--", alpha=0.3)

    return fig