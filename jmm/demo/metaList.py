from jmm.util.tushare_util import pro
import pandas as pd

df = pro.stock_basic(**{
    "ts_code": "",
    "name": "",
    "exchange": "",
    "market": "",
    "is_hs": "",
    "list_status": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "market",
    "list_date",
    "fullname",
    "enname",
    "cnspell",
    "exchange",
    "curr_type",
    "list_status",
    "delist_date",
    "is_hs"
])

assert isinstance(df, pd.DataFrame)
df.to_excel("metaList.xlsx")

