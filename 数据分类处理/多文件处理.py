import os
import csv
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
from pyecharts import Bar
from pyecharts import Line
import re
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def get_date_list(begin_date,end_date):
    date_list=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(begin_date,end_date))]
    return date_list
path="D:/Python/work/"
files=os.listdir(path)
print(files)
files_csv =list(filter(lambda x: x[-4:]=='.csv' , files))
files_csv.sort(key = lambda i:int(re.match(r'(\d+)',i).group()))
print(files_csv)
houselist=[]
for file in files_csv:
    with open(file,'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        prices=[row[2] for row in reader]
    for i in range(len(prices)):
        prices[i]=prices[i].replace('元/m²','')
        prices[i]=prices[i].replace('均价','') 
    while '' in prices:
        prices.remove('')
    prices = [ int(x) for x in prices ]
    print(prices)
    max_price =max(prices)
    min_price =min(prices)
    b=len(prices)
    sum=0
    for i in prices:
        sum=sum+i
        mid_price=sum/b
    print('钱塘新区二手房最高价格：%.2f元/平方米' % max_price)
    print("钱塘新区二手房最低价格：%.2f元/平方米" %min_price)
    print("钱塘新区二手房平均价格：%.2f元/平方米" %mid_price) 
    houselist.append('%.3f' %mid_price)
print(houselist)
v1=houselist
attr=get_date_list("2019-05-24","2019-11-12")
line=Line("房价数据变化")
line.add("房价",attr,v1,is_smooth=True,xaxis_rotate=50,mark_point=["average"])
line.show_config()
line.render()



















