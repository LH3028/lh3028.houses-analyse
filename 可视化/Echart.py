import os
import pandas as pd
import numpy as np
import csv
import re
from matplotlib import pyplot as plt
from pyecharts import Line
import sys
sys.setrecursionlimit(500000)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def get_date_list(begin_date,end_date):
    date_list=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(begin_date,end_date))]
    return date_list
def Sort(Key):
    path='D:/Python/Housedatas/'
    files=os.listdir(path)
    print(files)
    files_csv =list(filter(lambda x: x[-4:]=='.csv' , files))
    files_csv.sort(key = lambda i:int(re.match(r'(\d+)',i).group()))
    houselist=[]
    for file in files_csv:
        df=pd.read_csv(file)
        df=df[df['标题'].str.contains(Key)]
        print(df["均价"])
        prices=df["均价"].values
        for i in range(len(prices)):
            prices[i]=prices[i].replace('元/m²','')
            prices[i]=prices[i].replace('均价','')
        price = [ int(x) for x in prices ]
        print(price)
        max_price =max(price)
        min_price =min(price)
        b=len(price)
        sum=0
        for i in price:
            sum=sum+i
            mid_price=sum/b
        #print('钱塘新区二手房最高价格：%.2f元/平方米' % max_price)
        #print("钱塘新区二手房最低价格：%.2f元/平方米" %min_price)
        #print("钱塘新区二手房平均价格：%.2f元/平方米" %mid_price)
        houselist.append('%.3f' %mid_price)
    print(houselist)
    house=[float(i) for i in houselist]
    return house
path='D:/Python/housedatas/'
files=os.listdir(path)
print(files)
files_csv =list(filter(lambda x: x[-4:]=='.csv' , files))
files_csv.sort(key = lambda i:int(re.match(r'(\d+)',i).group()))
houselist=[]
for file in files_csv:
    with open(file,'r',encoding="UTF-8") as f:
        reader=csv.reader(f)
        prices=[row[2] for row in reader]
    for i in range(len(prices)):
        prices[i]=prices[i].replace('元/m²','')
        prices[i]=prices[i].replace('均价','')
    while '' in prices:
        prices.remove('')
    prices = [ int(x) for x in prices ]
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
house=[float(i) for i in houselist]
print(house)
house1=Sort("地铁")
house2=Sort("大学")
house3=Sort("车")
time=get_date_list("2020-02-14","2020-04-07")
x= Line("钱江新区房价变化图")
x.add("平均价格",time, house, mark_line=["average"], mark_point=["max", "min"],xaxis_name="日期",yaxis_name="价格",yaxis_name_gap=60)
x.add("地铁房",time,house1,mark_point=["max", "min"],xaxis_name="日期",yaxis_name="价格",yaxis_name_gap=60)
x.add("学区房",time,house2,mark_point=["max", "min"],xaxis_name="日期",line_color='green',yaxis_name="价格",yaxis_name_gap=60)
x.add("车位房",time,house3,mark_point=["max", "min"],xaxis_name="日期",yaxis_name="价格",yaxis_name_gap=60)
x.show_config()
x.render()