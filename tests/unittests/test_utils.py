import pytest
import pandas as pd
from unittest.mock import patch
from src.utils import min_max_normalisation, get_gp_name

def test_min_max_normalisation():
    series = pd.Series([1, 2, 3, 4, 5])
    expected = pd.Series([0.0, 0.25, 0.5, 0.75, 1.0])
    result = min_max_normalisation(series)
    pd.testing.assert_series_equal(result, expected)

def test_min_max_normalisation_single_value():
    series = pd.Series([5])
    expected = pd.Series([0.0])
    result = min_max_normalisation(series)
    pd.testing.assert_series_equal(result, expected)

def test_min_max_normalisation_identical_values():
    series = pd.Series([5, 5, 5, 5, 5])
    expected = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0])
    result = min_max_normalisation(series)
    pd.testing.assert_series_equal(result, expected)

@patch('src.utils.requests.get')
def test_get_gp_name_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'Organisation': {
            'Name': 'Test GP Practice'
        }
    }
    gp_code = 'A12345'
    result = get_gp_name(gp_code)
    assert result == 'Test GP Practice'

@patch('src.utils.requests.get')
def test_get_gp_name_failure(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    gp_code = 'A12345'
    result = get_gp_name(gp_code)
    assert result == 'Unknown'

@patch('src.utils.requests.get')
def test_get_gp_name_no_name(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'Organisation': {}
    }
    gp_code = 'A12345'
    result = get_gp_name(gp_code)
    assert result == 'Unknown'