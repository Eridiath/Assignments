"""This module has the goal of loading the data for use in other modules 
as well as saving the final results of the functions in other modules into a specific path.
    """

from pathlib import Path
import pandas as pd
from pandas import DataFrame

def load_data():
    """This function loads data from the main .tsv file. It loads all the available data
    and returns the data as is, for further data cleaning please use the clean_data
    method.
    """
    file_path = Path(__file__).parent / "data/eu_life_expectancy_raw.tsv"
    data_to_clean = pd.read_csv(file_path,
                                sep='\t|,', engine='python',header=0)
    return data_to_clean

def save_data(data_to_save: DataFrame):
    """This functions saves data to the pt_life_expectancy.csv file in the data folder.

    Args:
        data_to_save (DataFrame): This is the data to save, it should already have been
            cleaned prior to saving.
    """
    file_path = Path(__file__).parent / "data/pt_life_expectancy.csv"
    data_to_save.to_csv(file_path,
                   index=False)
    