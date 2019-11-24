import requests
from bs4 import BeautifulSoup
import csv
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
for i in range(1,50):
    link='http://www.fangchan.com/plus/nlist.php?q=%E6%88%BF%E4%BB%B7&tid=2&page='+str(i)
    r=requests.get(link,headers=headers)
    r.encoding='utf-8'
    soup=soup=BeautifulSoup(r.text,'lxml')
    print(r.text)
    house_list=soup.find_all('ul',class_="related-news-list")
    with open('house.csv', 'a',newline='',encoding='utf-8-sig')as csvfile:
        w=csv.writer(csvfile)
        w.writerow(('标题','时间','URL'))
        for i in house_list[0].find_all("li"):
            temp=[]
            name=i.find('a').get_text().strip()
            time=i.find('span').get_text()
            URL=i.find('a').get('href')
            temp=[name,time,URL]
            print(temp)
            w.writerow(temp)
     
     