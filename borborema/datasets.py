import pandas as pd


def load_geochemistry(path="data/geochemistry/whole_rock_geochemistry.csv"):
    """
    Load whole-rock geochemistry dataset.

    Parameters
    ----------
    path : str
        Path to the geochemistry CSV file.

    Returns
    -------
    pandas.DataFrame
        Dataframe containing whole-rock geochemical data.
    """
    return pd.read_csv(path)


def load_rb_sr(path="data/isotopes/rb_sr_isotopes.csv"):
    """
    Load Rb-Sr isotopic dataset.

    Parameters
    ----------
    path : str
        Path to CSV file containing Rb-Sr data.

    Returns
    -------
    pandas.DataFrame
        Dataframe containing Rb-Sr isotopic data.
    """
    return pd.read_csv(path)


def load_sm_nd(path="data/isotopes/sm_nd_isotopes.csv"):
    """
    Load Sm-Nd isotopic dataset.

    Parameters
    ----------
    path : str
        Path to CSV file containing Sm-Nd data.

    Returns
    -------
    pandas.DataFrame
        Dataframe containing Sm-Nd isotopic data.
    """
    return pd.read_csv(path)


def load_upb(path="data/geochronology/upb_ages.csv"):
    """
    Load U-Pb geochronology dataset.

    Parameters
    ----------
    path : str
        Path to CSV file containing zircon U-Pb ages.

    Returns
    -------
    pandas.DataFrame
        Dataframe containing U-Pb ages and uncertainties.
    """
    return pd.read_csv(path)