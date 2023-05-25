"""Module cleaning, used to select a country and obtain clean data from
    the .tsv file in the data folder.
    """
from dataclasses import dataclass
import argparse
import pathlib
from typing import Callable
import pandas as pd
from pandas import DataFrame
from life_expectancy.save import save_data
from life_expectancy.load import StrategyLoader, StrategyJSON,StrategyTSV
from life_expectancy.regions import Country

CleaningStrategy = Callable[[Country, DataFrame], DataFrame]

def clean_data_json(region_code:Country, data_to_clean:DataFrame):
    """This function receives data from the original .json file and cleans it for further
    usage.
    params:
        data_to_clean: pandas Dataframe - This is the data obtained from the .tsv file
            uncleaned and containing information from all regions and subjects.
        region_code: string - This is the country code for selecting the information
            wanted for usage. ex: PT for Portugal
    return: data: Pandas Datafrane - final dataframe containing the clean data from the
        origin and only containing data from the region selected
    """

    data_to_clean = data_to_clean.rename(columns={data_to_clean.columns[3]: "region"})
    data_to_clean = data_to_clean.rename(columns={data_to_clean.columns[5]: "value"})

    cleaned_data = data_to_clean.dropna()
    data = cleaned_data[cleaned_data['region'] == str(region_code)]
    return data

def clean_data_tsv(region_code:Country, data_to_clean:DataFrame):
    """This function receives data from the original .tsv file and cleans it for further
    usage.
    params:
        data_to_clean: pandas Dataframe - This is the data obtained from the .tsv file
            uncleaned and containing information from all regions and subjects.
        region_code: string - This is the country code for selecting the information
            wanted for usage. ex: PT for Portugal
    return: data: Pandas Datafrane - final dataframe containing the clean data from the
        origin and only containing data from the region selected
    """
    data_to_clean = data_to_clean.rename(columns={data_to_clean.columns[3]: "region"})
    data_to_clean = pd.melt(data_to_clean,id_vars=['unit','sex','age',"region"],var_name='year')
    data_to_clean = data_to_clean.astype({'year':'int'})
    data_to_clean['value'] = pd.to_numeric(data_to_clean.value.str.replace(r'[^\d.]',''),
                                               errors='coerce')

    cleaned_data = data_to_clean.dropna()
    data = cleaned_data[cleaned_data['region'] == str(region_code)]
    return data

@dataclass
class Pipeline:
    """Class created to orquestrate a pipeline for loading
    and cleaning and saving a generic data file."""
    loader: StrategyLoader
    cleaner: CleaningStrategy
    filepath: pathlib.Path

    def run(self, region_code: str) -> pd.DataFrame:
        """This function runs the Pipeline object in sequence
        requires only the region_code to provide to the functions
        inside.
        
        Args: region_code (str): region code to filter the cleaned data by
        """
        region = Country(region_code)
        data = self.loader.load_data(filepath=self.filepath)
        cleaned_data = self.cleaner(region, data)
        save_data(cleaned_data)
        return cleaned_data

def main(filename: str, region_code: str):
    """This is the main function in this script, it runs all other functions in sequence
    and receives the region code to feed those functions.

    Args:
        filename (str): Name of the file to obtain the raw data from, must contain the
            file extension
        region_code (str): This is the country code for selecting the information
            wanted for usage. ex: PT for Portugal
    """

    filepath = pathlib.Path(__file__).parent / 'data' / filename
    extension = filepath.suffix

    if extension == '.tsv':
        loader = StrategyTSV()
        clean_data = clean_data_tsv
    elif extension == '.zip':
        loader = StrategyJSON()
        clean_data = clean_data_json
    else:
        raise ValueError('Not tsv or zip file.')

    pipeline = Pipeline(loader=loader,cleaner=clean_data,filepath=filepath)
    pipeline.run(region_code=region_code)



if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Name of the file with the original data for use in clean_data")
    parser.add_argument("--region", help="The region code you wish to use in clean_data", type=str, choices=Country.get_list(),
                        default=Country.PT,required=False)
    args = parser.parse_args()
    main(args.name, args.region)
