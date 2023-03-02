"""Module cleaning, used to select a country and obtain clean data from
    the .tsv file in the data folder.
    """
import argparse
import pandas as pd
from pandas import DataFrame
from life_expectancy.save_load import save_data, load_data

def clean_data(region_code:str, data_to_clean:DataFrame):
    """This function receives data from the original .tsv file and cleans it for further
    usage.
    params:
        data_to_clean: pandas Dataframe - This is the data obtained from the .tsv file
            uncleaned and containing information from all regions and subjects.
        region_code: string - This is the country code for selecting the information
            wanted for usage. ex: PT for Portugal
    """

    data_to_clean = data_to_clean.rename(columns={data_to_clean.columns[3]: "region"})
    data_to_clean = pd.melt(data_to_clean,id_vars=['unit','sex','age',"region"],var_name='year')
    data_to_clean = data_to_clean.astype({'year':'int'})
    data_to_clean['value'] = pd.to_numeric(data_to_clean.value.str.replace(r'[^\d.]',''),
                                           errors='coerce')
    cleaned_data = data_to_clean.dropna()
    data = cleaned_data[cleaned_data['region'] == region_code]
    return data

def main(region_code: str):
    """This is the main function in this script, it runs all other functions in sequence
    and receives the region code to feed those functions.

    Args:
        region_code (str): This is the country code for selecting the information
            wanted for usage. ex: PT for Portugal
    """
    # print(region_code)
    # input("Press Enter to continue")
    data = load_data()
    cleaned_data = clean_data(region_code, data)
    save_data(cleaned_data)

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", help="The region code you wish to use in clean_data",
                        default='PT',required=False)
    args = parser.parse_args()
    main(args.region)
