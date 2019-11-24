# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:14:13 2014
@author: lifeix
"""
 
import urllib2
import re
from datetime import datetime
def craw1(keyword_name, startYear):
    a = keyword_name
    print (a,"\t")
    today = datetime.today()
    ye = today.year
    mon = today.month
    for year in range(startYear,ye + 1):
        month = 13
        if ye == year:
            month = mon
        for month in range(1,month):
            begintime = str(year) + "-" + "%02d"%month+"-01"
            endtime = str(year) + "-" + "%02d"%month+"-31"
            print (begintime, endtime)
            userMainUrl = "http://search.sina.com.cn/?time=custom&stime="+begintime+"&etime="+endtime+"&c=news&q="+a+"&sort=time&range=title"
            print (userMainUrl)
            req = urllib2.Request(userMainUrl)
            resp = urllib2.urlopen(req)
            respHtml = resp.read()
            urlpat = re.compile(r'<div class="l_v2">(.*?)</div>')
            match = urlpat.findall(respHtml)
            for numstr in match:
                searchnum = numstr[11:-2]
            print ("searchnum=",searchnum)
            
craw1('大学',2014)

