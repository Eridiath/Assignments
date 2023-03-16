"""Tests for the cleaning module"""
import pandas as pd
from unittest.mock import patch, Mock
from life_expectancy.cleaning import clean_data
from life_expectancy.save_load import save_data,load_data

@patch('life_expectancy.save_load.pd.read_csv')
def test_load_data(read_table_mock: Mock):
    """Testing the load_data function, this function runs read_csv to read
    the csv containing the raw_data for use, this is a native function and
    so we trust it works and only need to verify it is indeed called"""
    load_data()
    read_table_mock.assert_called_once()

@patch('life_expectancy.save_load.pd.DataFrame.to_csv')
def test_save_data(save_table_mock: Mock,goal_data_fixture):
    """Testing the save_data function, this function runs to_csv to save
    the Dataframe containing the cleaned data, this is a native function
    and so we trust it works and only need to verify it is indeed called"""
    save_data(goal_data_fixture)
    save_table_mock.assert_called_once()

def test_clean_data_function(source_data_fixture, goal_data_fixture):
    """This function tests the main function of the assignment"""
    results = clean_data('PT',source_data_fixture).reset_index(drop=True)
    pd.testing.assert_frame_equal(results,goal_data_fixture)
