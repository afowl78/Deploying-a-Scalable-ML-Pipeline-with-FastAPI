import pytest
import os
import pandas as pd
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_data_size():
    """
    Check that the data is sliced into a suitable size for testing.
    """
    with open('slice_output.txt', 'r') as file:
        lines = sum(1 for line in file)
    assert lines >= 2000



# TODO: implement the second test. Change the function name and input as needed
def test_features():
    """
    Check that all features are present in the data.
    """
    local_path = './data/census.csv'
    data = pd.read_csv(local_path)

    features = {
        'age', 'workclass', 'fnlgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'
    }

    assert set(data.columns) == features




# TODO: implement the third test. Change the function name and input as needed
def test_model():
    """
    # Check that the model is the RandomForestClassifier.
    """
    sample_x = [[1, 2, 3], [4, 5, 6]]
    sample_y = ['low', 'high']

    model = train_model(sample_x, sample_y)

    assert type(model) == type(RandomForestClassifier())
