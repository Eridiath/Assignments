""" Class with the goal of loading data in different formats
"""
from pathlib import Path
from abc import ABC, abstractmethod
import pandas as pd
from pandas import DataFrame

class StrategyLoader(ABC): # pylint: disable=too-few-public-methods
    """This class defines the strategy to be used for loading the
    files to clean. It can either be TSV or JSON files with the 
    associated strategies."""

    @abstractmethod
    def load_data(self,  filepath: Path) -> DataFrame:
        """Class must always have a function that loads data"""

class StrategyTSV(StrategyLoader): # pylint: disable=too-few-public-methods
    """Loading data from TSV file"""

    def load_data(self, filepath: Path) -> DataFrame:
        """This function loads data from the main .tsv file. It loads all the available data
        and returns the data as is, for further data cleaning please use the clean_data
        method.
        return data_to_clean - Pandas Dataframe: Dataframe obtained from loading the complete 
            data file.
        """

        data_to_clean = pd.read_csv(filepath,
                                    sep='\t|,', engine='python',header=0)
        return data_to_clean

class StrategyJSON(StrategyLoader): # pylint: disable=too-few-public-methods
    """Loading data from a JSON file, in this case also a zipped file"""

    def load_data(self, filepath: Path) -> DataFrame:
        """This function loads data from the zipped JSON file. It loads all the available data
        and returns the data as is, for further data cleaning please use the clean_data
        method.
        return data_to_clean - Pandas Dataframe: Dataframe obtained from loading the complete 
            data file.
        """

        data_to_clean = pd.read_json( # pylint: disable=no-member
            filepath,
            compression='infer').drop(
                columns=['flag','flag_detail']
            )

        return data_to_clean
