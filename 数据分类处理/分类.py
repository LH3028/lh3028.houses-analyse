import os
import csv
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import re
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def get_date_list(begin_date,end_date):
    date_list=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(begin_date,end_date))]
    return date_list
def Sort(Key):
    path='D:/Python/work/'
    files=os.listdir(path)
    print(files)
    files_csv =list(filter(lambda x: x[-4:]=='.csv' , files))
    files_csv.sort(key = lambda i:int(re.match(r'(\d+)',i).group()))
    print(files_csv)
    houselist=[]
    for file in files_csv:
        df=pd.read_csv(file)
        df=df[df['标题'].str.contains(Key)]
        print(df["均价"])
        prices=df["均价"].values
        for i in range(len(prices)):
            prices[i]=prices[i].replace('元/m²','')
            prices[i]=prices[i].replace('均价','') 
        print(prices)
        price = [ int(x) for x in prices ]
        print(price)  
        max_price =max(price)
        min_price =min(price)
        b=len(price)
        sum=0
        for i in price:
            sum=sum+i
            mid_price=sum/b
        print('钱塘新区二手房最高价格：%.2f元/平方米' % max_price)
        print("钱塘新区二手房最低价格：%.2f元/平方米" %min_price)
        print("钱塘新区二手房平均价格：%.2f元/平方米" %mid_price) 
        houselist.append('%.3f' %mid_price)
    print(houselist)
    house1=[float(i) for i in houselist]
    return house1
def house(files):
    path=files
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
        #print('钱塘新区二手房最高价格：%.2f元/平方米' % max_price)
        #print("钱塘新区二手房最低价格：%.2f元/平方米" %min_price)
        #print("钱塘新区二手房平均价格：%.2f元/平方米" %mid_price) 
        houselist.append('%.3f' %mid_price)
    #print(houselist)
    house2=[float(i) for i in houselist]
    print(house2)
    house1=Sort("地铁")
    house3=Sort("大学")
    house4=Sort("车")
    time=get_date_list("2019-05-24","2019-11-17")
    fig=plt.figure(dpi=150, figsize=(60,15))
    plt.plot(time,house1,'bs-',c='red',label='地铁')
    plt.plot(time,house2,'bs-',c='blue',label='平均价格')
    plt.plot(time,house3,'bs-',c='green',label='学区房')
    plt.plot(time,house4,'bs-',c='yellow',label='车位房')
    plt.legend(loc="upper left",fontsize=30)
    #设置图像的格式
    plt.title("钱塘新区房价变化",fontsize=50)
    plt.xlabel('日期',fontsize=25)
    plt.ylim(0,30000)
    plt.xticks(time,rotation=90)
    ylabel='\n'.join(('价','格'))
    plt.ylabel(ylabel,
               fontproperties='stkaiti',
               rotation='horizontal',
               fontsize=20,
               verticalalignment='bottom' )
    plt.tick_params(axis='both', which="major", labelsize=16)
    plt.savefig("house1.jpg")
    plt.show() 
    a=length(house1)
    b=length(house2)
    c=length(house3)
    
if __name__ == '__main__':
    house('D:/Python/work/')

 
   