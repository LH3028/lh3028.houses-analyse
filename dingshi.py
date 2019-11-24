import time
import datetime
import csv
import requests
from bs4 import BeautifulSoup
def pachong():
    headers={'User-Agent':'Request URL: https://hangzhou.anjuke.com/sale/qtxq/p1-rd1/'}
    for i in range(1,50):
        link='https://hangzhou.anjuke.com/sale/qtxq/p'+str(i)+'-rd1/#filtersort'
        r=requests.get(link,headers=headers) 
        soup=BeautifulSoup(r.text,'lxml')
        house_list=soup.find_all('li',class_="list-item")
        with open('602.csv', 'a',newline='',encoding='utf-8-sig')as csvfile:
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
    print("爬虫已经工作完毕!")
    time.sleep(60)
    nowtime()        
def main(h,m):
    if h ==9 and m ==2:
        pachong()
    elif h ==20  and m==10:
            pachong()
    else:
            print("稍安勿躁，爬虫正在等待时间。。。")
            time.sleep(60)
            nowtime()
            print("程序结束！")
            nowtime()
            
def nowtime():
    now=datetime.datetime.now()
    print(now.hour,now.minute)
    hour=now.hour
    minute=now.minute
    main(hour,minute)
nowtime()
    