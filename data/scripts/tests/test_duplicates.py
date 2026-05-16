import pandas as pd
from scripts.remove_duplicates import remove_duplicates

def test_duplicates_removed():

    input_file = "data/raw_dataset.csv"
    output_file = "data/processed_dataset.csv"

    cleaned_df = remove_duplicates(input_file, output_file)

    # Verify duplicates removed
    assert cleaned_df.duplicated().sum() == 0
