import os
import csv
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import re
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def get_date_list(begin_date,end_date):
    date_list=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(begin_date,end_date))]
    return date_list
def house(files):
    path=files
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
    time=get_date_list("2020-02-14","2020-04-09")
    with open('D:\\Python\\test\\predict1.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(time, house))
    fig=plt.figure(dpi=150, figsize=(63,15))
    plt.plot(time,house,'bs-',c='blue',label='价格')
    plt.legend(loc="upper left",fontsize=30)
    #设置图像的格式
    plt.title("钱塘新区房价变化",fontsize=50)
    plt.ylabel("价格",fontsize=30)
    plt.xlabel('日期',fontsize=20)
    plt.ylim(0,30000)
    plt.xticks(time,rotation=90)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=40)
    plt.tick_params(axis='both', which="major")
    plt.savefig("test.jpg")
    plt.show()
    fig=plt.figure(figsize=(20,6))
    plt.title("钱塘新区房价变化",fontsize=50)
    plt.ylabel("价格",fontsize=30)
    plt.xlabel('日期',fontsize=20)
    ax = fig.add_subplot(111)
    ax.scatter(time,house)
    plt.xticks(time,rotation=90)
    plt.savefig("test1.jpg")
    plt.show()
if __name__ == '__main__':
    house('D:/Python/Housedatas/')
   


