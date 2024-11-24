def min_max_normalisation(series):
    """
    Function to normalise a pandas series using min-max normalisation.

    Parameters
    ----------
    series : pandas.Series
        The series to normalise.
    
    Returns
    -------
    pandas.Series
        The normalised series.
    """
    return (series - series.min()) / (series.max() - series.min())