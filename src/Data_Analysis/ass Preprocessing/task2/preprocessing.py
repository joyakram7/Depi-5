import pandas as pd

def Drop_unnecessary_features(df, cols_to_drop):
    
    df = df.drop(cols_to_drop , axis = 1)
    return df


def Check_data_type(df):
    report = pd.DataFrame({
        "Data Type": df.dtypes,
        "Unique Values": df.nunique()
    })
    return report.transpose()