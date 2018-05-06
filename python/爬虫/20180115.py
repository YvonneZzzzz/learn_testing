'''
from urllib.request import urlopen
import chardet
import urllib2 

# html = urlopen("http://192.168.40.130:8089/index.html")
# html = urlopen("http://192.168.40.130:8089")
# html = urlopen("http://192.168.40.130:8089/index/")

line = "http://192.168.40.130:8089/index/" 
html_1 = urllib2.urlopen(line,timeout=30).read() 

mychar = chardet.detect(html_1) 

bianma = mychar['encoding'] 
#print bianma 
if bianma == 'utf-8' or bianma == 'UTF-8': 
#html=html.decode('utf-8','ignore').encode('utf-8') 
    html=html_1 
elif bianma == 'gbk' or bianma == 'GBK' : 
    html =html_1.decode('gbk','ignore').encode('utf-8') 
elif bianma == 'gb2312' : 
    html =html_1.decode('gb2312','ignore').encode('utf-8') 

print(html.read())
'''

'''py3爬虫抓取网页中文出现乱码
from urllib.request import urlopen

response = urlopen("http://192.168.40.130:8089/index/")
html = str(response.read(), 'utf-8')
print(html)
'''

from urllib.request import urlopen

# html = urlopen("http://192.168.40.130:8089/index.html")
# html = urlopen("http://192.168.40.130:8089")
html = urlopen("http://192.168.40.130:8089/index/")

html = str(html.read(),'utf-8')

# print(str(html.read(),'utf-8'))
# print(html.read())
print(html)






