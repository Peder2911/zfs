
import pandas as pd

raw = pd.read_excel("data/zf.xlsx",skiprows=1,sheet_name="ZF")
raw = raw.iloc[1:,slice(2,-2)]
raw.columns = (
            "dpto",
            "mpio",
            "mpio_cod",
            "vereda",
            "geotype",
            "zf",
            "area",
            "type",
            "objective",
            "tool",
            "lat",
            "lon"
        )

raw.dropna().to_csv("data/zf.csv", index = False)
