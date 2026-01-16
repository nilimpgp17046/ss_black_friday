import pandas as pd
import numpy as np
import zipfile

with zipfile.ZipFile("datasets.zip") as z:
  with z.open("walmart_data.csv") as f:
    df = pd.read_csv(f)

print(df)
  
