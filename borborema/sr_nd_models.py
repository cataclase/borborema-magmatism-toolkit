import numpy as np
import matplotlib.pyplot as plt


def dm_curve():
    """
    Generate depleted mantle εNd evolution curve.
    """

    tempo_ga = np.arange(0,4.6,0.1)

    epsilon_nd_dm = np.array([
8.5,8.2025,7.91,7.6225,7.34,7.0625,6.79,6.5225,6.26,6.0025,
5.75,5.5025,5.26,5.0225,4.79,4.5625,4.34,4.1225,3.91,3.7025,
3.5,3.3025,3.11,2.9225,2.74,2.5625,2.39,2.2225,2.06,1.9025,
1.75,1.6025,1.46,1.3225,1.19,1.0625,0.94,0.8225,0.71,0.6025,
0.5,0.4025,0.31,0.2225,0.14,0.0625
])

    return tempo_ga*1000, epsilon_nd_dm


def plot_eNd_age(age, end, suites, colors):
    """
    Plot εNd vs age diagram.
    """

    fig, ax = plt.subplots(figsize=(7,6))

    tempo_ma, epsilon_dm = dm_curve()

    ax.plot(tempo_ma, epsilon_dm, color="royalblue", label="DM")

    for serie,color in colors.items():

        mask = suites == serie

        ax.scatter(
            age[mask],
            end[mask],
            color=color,
            edgecolor="black",
            label=serie
        )

    ax.set_xlabel("Age (Ma)")
    ax.set_ylabel("εNd(t)")
    ax.legend()

    return fig