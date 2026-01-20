import sys

import pandas as pd

print('arguments:', sys.argv)

month = int(sys.argv[1])



df=pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_python pipeline.py 12{month}.parquet")

print(f'hello pipeline, month={month}')