import pandas as pd

df_path = "vif.dta"

df = None
with open(df_path, "r") as f:
    df = pd.read_stata(f)
    print df.head()