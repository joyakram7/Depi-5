import pandas as pd

def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File does not exist.")
        return None
    except Exception:
        print("Error: Could not read the file.")
        return None


df = Read_data_file("Titanic.csv")
print(df.head())