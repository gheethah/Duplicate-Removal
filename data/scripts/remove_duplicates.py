import pandas as pd

def remove_duplicates(input_file, output_file):

    # Read dataset
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    cleaned_df = df.drop_duplicates()

    # Save cleaned dataset
    cleaned_df.to_csv(output_file, index=False)

    return cleaned_df


if __name__ == "__main__":

    remove_duplicates(
        "data/raw_dataset.csv",
        "data/processed_dataset.csv"
    )
