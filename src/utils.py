import requests

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

def get_gp_name(gp_code : str) -> str:
    """
    Function to get the name of a GP practice from the NHS Spine Organisation Data Service (ODS) API.

    Parameters
    ----------
    gp_code : str
        The GP practice code to look up.

    Returns
    -------
    str
        The name of the GP practice.
    """
    url = f"https://directory.spineservices.nhs.uk/ORD/2-0-0/organisations/{gp_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('Organisation', {}).get('Name', 'Unknown')
    else:
        return 'Unknown'