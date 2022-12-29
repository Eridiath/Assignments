"""Module cleaning, used to select a country and obtain clean data from
    the .tsv file in the data folder and then save the result in the same
    folder.
    """
import argparse
import pandas as pd

def clean_data(region_code:str):
    """This is the only function in the cleaning module, it collects the
    data from the main .tsv file, unpivots it and saves the data in a csv
    file, you may also pass in a region code to obtain information on that
    region, the default is PT.
    """
    data_to_clean = pd.read_csv('/nfs/workstation/sb_tom_004/tom_ads/foundations_repo/assignments/life_expectancy/data/eu_life_expectancy_raw.tsv',
                                sep='\t|,', engine='python',header=0)
    data_to_clean = data_to_clean.rename(columns={data_to_clean.columns[3]: "region"})
    data_to_clean = pd.melt(data_to_clean,id_vars=['unit','sex','age',"region"],var_name='year')
    data_to_clean = data_to_clean.astype({'year':'int'})
    data_to_clean['value'] = pd.to_numeric(data_to_clean.value.str.replace(r'[^\d.]',''),
                                           errors='coerce')
    cleaned_data = data_to_clean.dropna()
    pt_data = cleaned_data[cleaned_data['region'] == region_code]
    pt_data.to_csv('/nfs/workstation/sb_tom_004/tom_ads/foundations_repo/assignments/life_expectancy/data/pt_life_expectancy.csv',
                   index=False)

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("region", help="The region code you wish to use in clean_data",default='PT')
    args = parser.parse_args()
    clean_data(args.region)
