from pathlib import Path

"""File to store and generate mock datasets
    Inspired by the work of Gabriela Sá Martins.
    """

def raw_data() -> dict:
    """Function used to retrieve mock raw data

    Returns:
        dict: Dictionary containing the data
    """

    data = {
        'unit': ['YR', 'YR', 'YR'],
        'sex': ['F', 'F', 'F'],
        'age': ['Y1', 'Y1', 'Y1'],
        'geo\time': ['AM', 'AL', 'PT'],
        '2021': ['79.4', '80.4', '80.2'],
        '2020': ['79.1', '79.2', '78.5'],
        '2019': ['82.9', '83.5', '83.3']
    }
    return data

def expect_data() -> dict:
    """Function used to return the treated data that
    comes from the raw data defined in raw_data()

    Returns:
        dict: dict with clean data from raw_data()
    """

    data = {
        'unit': ['YR', 'YR', 'YR'],
        'sex': ['F', 'F', 'F'],
        'age': ['Y1', 'Y1', 'Y1'],
        'region': ['PT', 'PT', 'PT'],
        'year': [2021, 2020, 2019],
        'value': [80.2, 78.5, 83.3]
    }
    return data

def json_data() -> dict:
    """Function used to retrieve mock raw data

    Returns:
        dict: Dictionary containing the data
    """
    
    data = {
        'unit': ['YR', 'YR', 'YR'],
        'sex': ['F', 'F', 'F'],
        'age': ['Y1', 'Y1', 'Y1'],
        'geo\time': ['PT', 'PT', 'PT'],
        'year': [2021, 2020, 2019],
        'life_expectancy': [80.2, 78.5, 83.3]
    }
    return data

def json_filepath() -> Path:
    """
    Function used to define a file path to the json
    file."""

    filepath = Path(__file__).parent.parent / 'data/eurostat_life_expect.zip'
    return filepath

def tsv_filepath() -> Path:
    """
    Function used to define a file path to the tsv
    file."""
    
    filepath = Path(__file__).parent.parent / 'data' / 'pt_life_expectancy.csv'
    return filepath

def goal_filepath() -> Path:
    """
    Function used to define a file path to the saved file"""
    
    filepath = Path(__file__).parent.parent / 'data' / 'pt_life_expectancy.csv'
    return filepath