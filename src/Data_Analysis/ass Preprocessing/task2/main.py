import pandas as pd
from preprocessing import Drop_unnecessary_features, Check_data_type
from config import data_path, cols_to_drop


def main():
    df = pd.read_csv(data_path)
    print("Before:", df.columns.tolist())

    df = Drop_unnecessary_features(df, cols_to_drop)
    print("After:", df.columns.tolist())

    report = Check_data_type(df)
    print(report)


if __name__ == "__main__":
    main()