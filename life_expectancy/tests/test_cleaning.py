"""Tests for the cleaning module"""
import pandas as pd
import pathlib
from unittest.mock import patch, Mock
from life_expectancy.cleaning import clean_data_tsv,clean_data_json
from life_expectancy.save import save_data
from life_expectancy.load import StrategyJSON,StrategyTSV
from life_expectancy.regions import Country

@patch('life_expectancy.load.pd.read_csv')
def test_load_data_TSV(read_table_mock: Mock, source_tsv_filepath):
    """Testing the load_data function, this function runs read_csv to read
    the csv containing the raw_data for use, this is a native function and
    so we trust it works and only need to verify it is indeed called"""
    test_instance = StrategyTSV()
    test_instance.load_data(filepath=source_tsv_filepath)
    read_table_mock.assert_called_once()

@patch('life_expectancy.load.pd.read_json')
def test_load_data_JSON(read_table_mock: Mock, source_json_filepath):
    """Testing the load_data function, this function runs read_josn to read
    the zip containing the raw_data for use, this is a native function and
    so we trust it works and only need to verify it is indeed called"""
    test_instance = StrategyJSON()
    test_instance.load_data(filepath=source_json_filepath)
    read_table_mock.assert_called_once()

@patch('life_expectancy.save.DataFrame.to_csv')
def test_save_data(save_table_mock: Mock,goal_data_fixture, goal_data_filepath):
    """Testing the save_data function, this function runs to_csv to save
    the Dataframe containing the cleaned data, this is a native function
    and so we trust it works and only need to verify it is indeed called"""
    save_data(goal_data_fixture,filepath=goal_data_filepath)
    save_table_mock.assert_called_once()

def test_clean_data_tsv_function(source_data_fixture, goal_data_fixture):
    """This function tests the main function of the assignment"""
    results = clean_data_tsv(Country.PT,source_data_fixture).reset_index(drop=True)
    pd.testing.assert_frame_equal(results,goal_data_fixture)

def test_clean_data_json_function(source_json_data_fixture, goal_data_fixture):
    """This function tests the main function of the assignment"""
    results = clean_data_json(Country.PT,source_json_data_fixture)
    pd.testing.assert_frame_equal(results,goal_data_fixture)
    
def test_enum():
    """Tests the enum with the country names and codes"""
    countries_list = Country.get_list()
    countries_exp = [
        'AUSTRIA',
        'BELGIUM',
        'BULGARIA',
        'SWITZERLAND',
        'CYPRUS',
        'CZECHIA',
        'DENMARK',
        'ESTONIA',
        'GREECE',
        'SPAIN',
        'FINLAND',
        'FRANCE',
        'CROACIA',
        'HUNGARY',
        'ICELAND',
        'ITALY',
        'LIECHTENSTEIN',
        'LITHUANIA',
        'LUXEMBOURG',
        'LATVIA',
        'MALTA',
        'NETHERLANDS',
        'NORWAY',
        'POLAND',
        'PORTUGAL',
        'ROMANIA',
        'SWEDEN',
        'SLOVENIA',
        'SLOVAKIA',
        'GERMANY',
        'ALBANIA',
        'IRELAND',
        'MONTENEGRO',
        'NORTH_MACEDONIA',
        'SERBIA',
        'ARMENIA',
        'AZERBAIJAN',
        'GEORGIA',
        'TURKEY',
        'UKRAINE',
        'BELARUS',
        'UNITED_KINGDOM',
        'KOSOVO',
        'FRANCE_METROPOLITAN',
        'MOLDOVA',
        'SAN_MARINO',
        'RUSSIA'
    ]
    assert not set(countries_list) ^ set(countries_exp)
