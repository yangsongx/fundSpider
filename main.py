# -*- coding: utf-8 -*-

from fund_list import get_fund_list
from fund_info import FuncInfo
# from tqdm import tqdm
import os
from p_tqdm import p_umap
import time
import datetime

csv_data_dir = "./output/csv_data"

#start_date, end_date = "2021-03-14", time.strftime("%Y-%m-%d", time.localtime())
start_date, end_date = (datetime.datetime.now() - datetime.timedelta(days = 2)).strftime("%Y-%m-%d"), (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%Y-%m-%d")

print(start_date)
print(end_date)

#start_date, end_date = "2021-03-14", time.strftime("%Y-%m-%d", time.localtime())


def get_fund(fund):
    code = fund.get("code")
    # name = fund.get("name")
    file_name = os.path.join(csv_data_dir, u"%s.csv" % code)
    if not os.path.exists(csv_data_dir):
        os.mkdir(csv_data_dir)
    if os.path.isfile(file_name):
        return
    info = FuncInfo(code=code)
    info.load_net_value_info(start_date, end_date)
    df = info.get_data_frame()
    df.to_csv(file_name)


if __name__ == '__main__':
    # 抓取全量基金 start_date~end_date净值数据
    fund_list = get_fund_list()
    fund_num = len(fund_list)
    print("total fund: %s" % fund_num)
    p_umap(get_fund, fund_list)
