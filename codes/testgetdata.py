#%%
import akshare as ak
import pandas as pd
# %% 获取基本信息
fund_individual_basic_info_xq_df = ak.fund_individual_basic_info_xq(symbol="001938")
print(fund_individual_basic_info_xq_df)
# %% 获取历史行情
fund_net_value_df = ak.fund_open_fund_info_em(
    symbol="001938",
    indicator="单位净值走势")
fund_net_value_df["净值日期"] = pd.to_datetime(fund_net_value_df["净值日期"])
filtered_df = fund_net_value_df[fund_net_value_df["净值日期"] >= "2019-01-01"]
filtered_df = filtered_df.set_index("净值日期", drop=True)
print(filtered_df)