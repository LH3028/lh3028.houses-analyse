import requests,time
from lxml import etree


def Redirect(url):
    try :
        res = requests.get(url,timeout=10)
        url = res.url
    except Exception as e:
        print('4',e)
        time.sleep(1)
    return url

def baidu_search(wd,pn_max,sav_file_name):
    url = 'http://www.baidu.com/s'
    return_set = set()

    for page in range(pn_max):
        pn = page*10
        querystring = {'wd':wd,'pn':pn}
        headers = {
            'pragma':'no-cache',
            'accept-encoding': 'gzip,deflate,br',
            'accept-language' : 'zh-CN,zh;q=0.8',
            'upgrade-insecure-requests' : '1',
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'cache-control': "no-cache",
            'connection': "keep-alive",
        }

        try :
            response = requests.request('GET',url,headers=headers,params=querystring)
            print('!!!!!!!!!!!!!!',response.url)
            selector = etree.HTML(response.text,parser = etree.HTMLParser(encoding='utf-8'))
        except Exception as e:
            print('页面加载失败',e)
            continue
        with open(sav_file_name,'a+') as f:
            for i in range(1,10):
                try :
                    context = selector.xpath('//*[@id="'+str(pn+i)+'"]/h3/a[1]/@href')
                    
                    print(len(context),context[0])
                    i = Redirect(context[0])
                    print('context='+context[0])
                    print ('i='+i)
                    f.write(i)
                    f.write('\n')
                    break
                    return_set.add(i)
                    f.write('\n')
                except Exception as e:
                    print(i,return_set)
                    print('3',e)

    return return_set

if __name__ == '__main__':
    wd = '房价政策'
    pn = 100
    save_file_name = 'new.txt'
    return_set = baidu_search(wd,pn,save_file_name)