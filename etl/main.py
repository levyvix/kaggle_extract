import pandas as pd

if __name__ == "__main__":
    df = pd.read_parquet(
        "C:\\Users\\levyv\\Desktop\\proj\\kaggle_extract\\data\\events.parquet"
    )

    print(df.head())
