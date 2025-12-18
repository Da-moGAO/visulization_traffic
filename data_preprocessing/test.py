import pandas as pd
from extract_data import extract_data

data_dir = extract_data()

data1 = pd.read_csv(list(data_dir.values())[0])
print(data1.head())
