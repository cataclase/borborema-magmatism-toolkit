import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def run_pca(df, variables):
    """
    Perform Principal Component Analysis on geochemical data.

    Parameters
    ----------
    df : pandas.DataFrame
        Geochemical dataset.

    variables : list
        List of geochemical variables.

    Returns
    -------
    PC : ndarray
        PCA scores.

    loadings : ndarray
        PCA loadings.

    explained_variance : ndarray
        Variance explained by each component.
    """

    X = df[variables].values

    X_scaled = StandardScaler().fit_transform(X)

    pca = PCA(n_components=2)

    PC = pca.fit_transform(X_scaled)

    loadings = pca.components_.T

    return PC, loadings, pca.explained_variance_ratio_


def plot_pca(PC, loadings, variables, suites, colors):
    """
    Plot PCA biplot.

    Parameters
    ----------
    PC : ndarray
        PCA scores.

    loadings : ndarray
        PCA loadings.

    variables : list
        Geochemical variables.

    suites : array-like
        Magmatic suite labels.

    colors : dict
        Color mapping for suites.

    Returns
    -------
    matplotlib.figure.Figure
    """

    fig, ax = plt.subplots(figsize=(8,7))

    for serie, color in colors.items():

        mask = suites == serie

        ax.scatter(
            PC[mask,0],
            PC[mask,1],
            s=70,
            color=color,
            edgecolor="black",
            linewidth=0.4,
            label=serie
        )

    pc_range = max(abs(PC[:,0]).max(), abs(PC[:,1]).max())

    scale = pc_range * 0.85

    for i, element in enumerate(variables):

        x = loadings[i,0] * scale
        y = loadings[i,1] * scale

        ax.arrow(
            0,0,x,y,
            color="black",
            linewidth=1.4,
            head_width=0.18
        )

        ax.text(x*1.15, y*1.15, element)

    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")

    ax.axhline(0,color="gray",lw=0.8)
    ax.axvline(0,color="gray",lw=0.8)

    ax.legend()

    plt.tight_layout()

    return fig