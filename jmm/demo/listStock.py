from jmm.util.tushare_util import pro

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
    "list_date"
])
print(df)


