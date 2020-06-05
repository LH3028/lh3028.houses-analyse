# lh3028.github.io
钱塘新区房价数据爬取分析可视化
=======





#### 1、背景

​       2019年4月4日：[钱塘新区](https://baike.baidu.com/item/%E9%92%B1%E5%A1%98%E6%96%B0%E5%8C%BA/23377723?fr=aladdin)成立。

​       杭州钱塘新区规划控制总面积531.7平方公里，空间范围包括杭州大江东产业集聚区和现杭州经济技术开发区，托管管理范围包括江干区的下沙、白杨2个街道，萧山区的河庄、义蓬、新湾、临江、前进5个街道，以及杭州大江东产业集聚区规划控制范围内的其他区域（不含党湾镇所辖接壤区域的行政村）

​      地理位置：大江东产业集聚区与杭州经济技术开发区位于杭州东隅、钱塘江下游要冲。 杭州钱塘新区其中之一的大江东产业集聚区紧邻杭州主城区，处于环杭州湾“V”字型产业带的拐点，是环杭州湾战略要地和杭州城市发展的战略地带。杭州钱塘新区其中之一的杭州经济技术开发区地理位置优越，位于杭州东部，钱塘江北岸，长江三角洲南翼，东临海宁市，南濒钱塘江，西靠主城区。



#### 2、政治

​        杭州钱塘新区建设要坚持以习近平新时代中国特色社会主义思想为指导，深入贯彻党的十九大和省第十四次党代会精神，全方位融入长三角一体化发展国家战略，全面落实省委、省政府“四大建设”决策部署，高效发挥杭州经济技术开发区等国家级平台的带动作用，优化资源配置，强化科技创新，加快转型升级，着力打造世界级智能制造产业集群、长三角地区产城融合发展示范区、全省标志性战略性改革开放大平台、杭州湾数字经济与高端制造融合创新发展引领区。 

​      钱塘新区设施完善，有第一产业、第二产业，教育事业和医疗卫生抓根于此。 新区内拥有杭州医药港小镇、广汽乘用车（杭州）公司、西子航空工业公司、柔性电子与智能技术全球研究中心等平台和企业，在生物医药、汽车及零部件、航空航天、新能源新材料等产业上具备市场竞争优势。各类学校60多所。其中大学14所，中学8所，小学13所，幼儿园31所。各类卫生机构66个，拥有三甲医院2家。它是杭州版的“浦东新区”。



#### 3、对房价影响

​       钱塘新区目前人才引进，工业园区多，工人住房租房需求量大，价格暂时不会受到数码影响。虽价格优势明显，但不管是自住还是投资，建议购房者选择交通便利、配套好、资源丰富的“硬核”地段。如果市场波动，这些将成为房子抗跌的重要因素。同时，钱塘新区发展的时间轴很长，购房者也不要期望值过高。 但是从长远角度来看，未来钱塘新区的发展空间很大。所以房价目前没有波动，但是就经济发展来看，钱塘新区的未来不可估量，房价可能在未来一段时间有很大增幅。所以钱塘新区的房价数据是一个很好的研究对象和可视化处理对象。



#### 4、可视化研究流程

​            通过爬虫收集安居客官网上有关钱塘新区房价变化的数据

![image-20200518101114091](https://i.loli.net/2020/06/05/CSzBx7adViFUkng.png)



通过Python爬虫将爬取的数据以csv形式存储

```python 
import requests
import csv
from bs4 import BeautifulSoup
headers={'User-Agent':'Request URL: https://hangzhou.anjuke.com/sale/qtxq/p1-rd1/'}
for i in range(1,50):
   link='https://hangzhou.anjuke.com/sale/qtxq/p'+str(i)+'-rd1/#filtersort'
   r=requests.get(link,headers=headers) 
   soup=BeautifulSoup(r.text,'lxml')
   house_list=soup.find_all('li',class_="list-item")
   with open('12.07.csv', 'a',newline='',encoding='utf-8-sig')as csvfile:
        w=csv.writer(csvfile)
        w.writerow(('标题','价格','均价','房子大小','总面积','楼层','优点'))
        for house in house_list:
            temp =[] 
            name=house.find('div',class_='house-title').a.text.strip()
            price=house.find('div',class_='pro-price').strong.text.strip()
            price_ave=house.find('div',class_='pro-price').contents[2].text.strip()
            area=house.find('div',class_='details-item').contents[1].text
            area_house=house.find('div',class_='details-item').contents[3].text
            floor=house.find('div',class_='details-item').contents[5].text
            advantages=house.find('div',class_='tags-bottom').text.strip()
            temp=[name,price,price_ave,area,area_house,floor,advantages]
            print(temp)
            w.writerow(temp)
```


![image-20200604194308354.png](https://i.loli.net/2020/06/05/HeK485XaGC17gBQ.png)



对爬取的csv表格数据价格进行一系列的数据处理和清洗

```Python
import csv
from matplotlib import pyplot as plt
import pandas as pd
filename ='D:\\Python\\CSV\\11.20.csv'
with open(filename,'r',encoding='utf-8') as f:
    reader=csv.reader(f)
    prices=[row[1] for row in reader]
    print(prices)
    for i in prices:
        prices.remove('价格')
        print(prices)
print(len(prices))
print(prices)
price=[float(i) for i in prices]
print(price)
def averagenum(list):
    sum=0
    for item in list:
        sum+=item
        return sum/len(list)
        print(averagenum(price))
fig=plt.figure(dpi=150, figsize=(30,10))
plt.plot(price,c='blue')
#设置图像的格式
plt.title("House Prices",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylim(100,400)
plt.ylabel("price",fontsize=10)
plt.tick_params(axis='both', which="major", labelsize=16)
plt.show()
```



对价格数据进行初步可视化

![image-20200518101536583]( https://i.loli.net/2020/06/05/HVJ5oSaKC6crU9j.png)

发现对价格数据进行分析实际意义不大，没有可比性。丢弃原来的思路，重新找一个研究方向。

对均价一列数据进行数据处理、清洗和分析。

![image-20200518101624556](https://i.loli.net/2020/06/05/x1nvDGVu5HftPdT.png)

去除均价一列除数字之外的字符串，输出一个只有数字的列表

```Python
for i in range(len(prices)):
        prices[i]=prices[i].replace('元/m²','')
        print(prices[i])
print(prices)

```

把列表中的数据转换为int类型

```python
a=[int(i) for i in prices]
print(a)
```

对均价数据简单可视化处理

利用常用的Python可视化库对数据进行可视化处理，常用的Python可视化库有Matplotlib\

```Python
from pyecharts import Line
import numpy as np 
a=[int(i) for i in prices]
print(a)
v1=a
attr=list(range(0,2940))
line=Line("房价数据变化")
line.add("9.18",attr,v1,is_smooth=True,mark_point=["average"])
line.show_config()
line.render()
```



![image-20200518101745449](https://i.loli.net/2020/06/05/ljMKfaXxebkcBVE.png)

把均价数据进行分类可视化处理

```python 
#-*- coding:utf-8 -*-
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
    path='D:\Python\Housedatas'
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
    time=get_date_list("2020-02-14","2020-05-05")
    house1=Sort("地铁")
    house3=Sort("大学")
    house4=Sort("车")
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
    plt.savefig("house2.jpg")
    plt.show() 
if __name__ == '__main__':
    house('D://Python//Housedatas')
```

![image-20200518102044482](https://i.loli.net/2020/06/05/AhfOoeXRpvkyw17.png)

![image-20200518102148518](https://i.loli.net/2020/06/05/ItUCnGEXBRjfL5M.png)



对房价数据进行预测分析

```python 
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import matplotlib.pylab as plt 
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
df = pd.read_csv('D://Python//test//predict1.csv', header=0, names=["日期","房价"])
time=df['日期']
house=df['房价']
ts_log = np.log(df["房价"])
def draw_acf_pacf(ts,lags):
    f = plt.figure(facecolor='white')
    ax1 = f.add_subplot(211)
    plot_acf(ts,ax=ax1,lags=lags)
    ax2 = f.add_subplot(212)
    plot_pacf(ts,ax=ax2,lags=lags)
    plt.subplots_adjust(hspace=0.5)
    plt.show()
def get_date_list(begin_date,end_date):
    date_list=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(begin_date,end_date))]
    return date_list
draw_acf_pacf(ts_log,30)
rol_mean = ts_log.rolling(window=12).mean()
rol_mean.dropna(inplace=True)
ts_diff_1 = rol_mean.diff(1)
ts_diff_1.dropna(inplace=True)
model = ARIMA(ts_log, order=(0,1,1)) 
result_arima = model.fit( disp=-1, method='css')
predict_ts = result_arima.predict()

# 一阶差分还原

diff_shift_ts = ts_diff_1.shift(1)
diff_recover_1 = predict_ts.add(diff_shift_ts)

# 再次一阶差分还原

rol_shift_ts = rol_mean.shift(1)
diff_recover = diff_recover_1.add(rol_shift_ts)

# 移动平均还原

rol_sum = ts_log.rolling(window=11).sum()
rol_recover = diff_recover*12 - rol_sum.shift(1)

# 对数还原

log_recover = np.exp(rol_recover)
log_recover.dropna(inplace=True)
data=data[log_recover.index]  # 过滤没有预测的记录plt.figure(facecolor='white')
time=get_date_list("2020-02-28","2020-04-23")
plt.figure(figsize=(30,8))
plt.title("钱塘新区房价预测",size=20)
plt.xlabel("时间",size=15)
plt.ylabel("价格",rotation=90,size=15)

plt.plot(time,data,color='red', label='Predict')
plt.plot(time,log_recover,color='blue', label='Original')
plt.xticks(time,rotation=90)
plt.legend(loc='best',fontsize='x-large')
plt.savefig("predict.jpg")
plt.show()
```

![image-20200518102409762](https://i.loli.net/2020/06/05/sozQTnxeDwa1KWJ.png)

把均价数据与其他数据联系并进行可视化处理



```Python
import os
import csv
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import re
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
path='D:\Python\Housedatas'
files=os.listdir(path)
print(files)
files_csv =list(filter(lambda x: x[-4:]=='.csv' , files))
houselist=[]
def Sort(Key):
    path="D://Python//Housedatas"
    files=os.listdir(path)
    print(files)
    files_csv =list(filter(lambda x: x[-4:]=='.csv' , files))
    files_csv.sort(key = lambda i:int(re.match(r'(\d+)',i).group()))
    houselist=[]
    c=0
    for file in files_csv:
        df=pd.read_csv(file)
        df=df[df['标题'].str.contains(Key)]
        #print(df["均价"])
        prices=df["均价"].values
        for i in range(len(prices)):
            prices[i]=prices[i].replace('元/m²','')
            prices[i]=prices[i].replace('均价','') 
        price = [ int(x) for x in prices ]
        print(price)  
        max_price =max(price)
        min_price =min(price)
        b=len(price)
        c+=b
        sum=0
        for i in price:
            sum=sum+i
            mid_price=sum/b         #每天的房价均价
        #print('钱塘新区二手房最高价格：%.2f元/平方米' % max_price)
        #print("钱塘新区二手房最低价格：%.2f元/平方米" %min_price)
        #print("钱塘新区二手房平均价格：%.2f元/平方米" %mid_price) 
        houselist.append('%.3f' %mid_price)
    #print(houselist)
    house=[float(i) for i in houselist]
    print(house)
    a=len(house)
    sum=0
    for i in house:
        sum=sum+i
        mid_house=sum/a
    print(mid_house)
    return c     #换为round(mid_house,3)，则求各类房子的均价
A=Sort("地铁")
B=Sort("上学")
C=Sort("江景")
D=Sort("车位")
E=Sort("精装")
F=Sort("阳台")
```

```python 
from pyecharts import Pie
attr =["地铁房", "学区房", "江景房", "车位房", "精装房", "阳台房"]
v1 =[A, B, C, D, E, F]
pie =Pie("频次饼图",title_pos = 'center')
pie.add("", attr, v1, is_label_show=True,
        legend_orient = 'vertical', #图例垂直
        legend_pos = 'left'
       )
pie.render(r"频次饼图.html")
```

![image-20200518102647653](https://i.loli.net/2020/06/05/pcU7wRlVzLoTZhm.png)

![image-20200518102710159](https://i.loli.net/2020/06/05/6fErQhxOmIotvPg.png)

![image-20200518102753579](https://i.loli.net/2020/06/05/1zY3PiEk6tAF4p9.png)


![image-20200604195812716.png](https://i.loli.net/2020/06/05/5E8zCh4jcyfFxbA.png)




最后把所有的数据通过网页的形式展现出来（http://47.97.213.17:8080/houses/index.html）。


![image-20200604195918554.png](https://i.loli.net/2020/06/05/hZOQqarUFMBCbmK.png)

