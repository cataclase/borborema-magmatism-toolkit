import pandas as pd
import numpy as np
import re
import unicodedata


def strip_accents(s):
    """
    Remove accents from a string.

    Parameters
    ----------
    s : str
        Input string.

    Returns
    -------
    str
        String without diacritics.
    """
    s = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def normalize_series(x):
    """
    Standardize names of magmatic suites.

    Parameters
    ----------
    x : str
        Raw suite name.

    Returns
    -------
    str
        Normalized suite name.
    """

    if pd.isna(x):
        return np.nan

    s = strip_accents(str(x)).lower()
    key = re.sub("[^a-z]", "", s)

    mapping = {
        "alk": "Alk",
        "phkcalcalk": "PHKCalcAlk",
        "ehkcalcalk": "EHKCalcAlk",
        "chalk": "ChAlk",
        "shos": "Shos",
        "archean": "Archean",
        "paleoproterozoic": "Paleoproterozoic"
    }

    return mapping.get(key, x)


def clean_numeric(x):
    """
    Convert numeric strings to float.

    Removes commas, spaces and invalid characters.

    Parameters
    ----------
    x : str

    Returns
    -------
    float
    """

    if pd.isna(x):
        return np.nan

    x = str(x).replace(",", ".")
    x = re.sub(r"[^0-9eE\+\-\.]", "", x)

    if x == "":
        return np.nan

    return float(x)