
import pandas as pd


survey = pd.read_csv("data/merged_data_PDET.csv",encoding="latin1")
zf = pd.read_csv("data/zf.csv")

zf = zf[zf["geotype"] != "VEREDA DANE"]
print(zf)

zeropad = lambda n: "{:08d}".format(int(n))
survey["mpio_cod"] = survey["p2_cod"].apply(zeropad)
zf["mpio_cod"] = zf["mpio_cod"].apply(zeropad)

survey["zf"] = (survey["mpio_cod"]
        .apply(lambda c: c in zf["mpio_cod"].unique())
    )

# Is Muni. capital
print((survey["zf"] & (survey["p3_zona"] == 1)).sum())

# To match...
print((survey["zf"] & (survey["p3_zona"] == 2)).sum())

