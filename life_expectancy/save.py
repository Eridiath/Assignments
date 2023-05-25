"""This module has the goal of saving the final results of the functions in other modules
into a specific path.
    """

from pathlib import Path
from pandas import DataFrame

def save_data(data_to_save: DataFrame):
    """This functions saves data to the pt_life_expectancy.csv file in the data folder.

    Args:
        data_to_save (DataFrame): This is the data to save, it should already have been
            cleaned prior to saving.
    """
    file_path = Path(__file__).parent / "data/pt_life_expectancy.csv"
    data_to_save.to_csv(file_path,
                   index=False)
    