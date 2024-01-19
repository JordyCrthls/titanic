import numpy as np
import pandas as pd


def factorize_columns(data, columns_to_factorize):
    encoded_mappings = {}

    for column in columns_to_factorize:
        codes, unique_values = pd.factorize(data[column])
        data[column] = codes
        encoded_mappings[column] = {column: unique_values}

    return data, encoded_mappings


def replace_undefined_with_mode(data, column_name):
    if column_name in data.columns:
        mode_value = data[column_name].mode()[0]
        data[column_name] = data[column_name].replace(np.nan, mode_value)
        data[column_name] = data[column_name].replace(-1, mode_value)
    else:
        print(f"The column '{column_name}' does not exist in the DataFrame.")
    return data


def clean_data(data):
    data.drop(['Name', 'PassengerId', 'Cabin', 'Parch', 'SibSp', 'Ticket', 'Fare'], axis=1, inplace=True)
    data, mappings = factorize_columns(data, data.columns)

    for col in data.columns:
        data = replace_undefined_with_mode(data, col)

    return data


def read_data():
    return pd.read_csv("Titanic-Dataset.csv")


def get_clean_data():
    df = read_data()
    return clean_data(df)
