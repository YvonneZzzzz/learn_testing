import requests
from bs4 import BeautifulSoup

# 请求博客首页
r = requests.get('http://www.cnblogs.com/yoyoketang/')

# 打印出blog的内容
blog = r.content
# 用html.parser解析html
soup = BeautifulSoup(blog, "html.parser")

def fun1():
    # 读取时间
    # 获取所有的class属性为dayTitle，返回Tag类
    times = soup.find_all(class_="dayTitle")
    for i in times:
        a = i
        # 获取a标签的文本
        print (i.a.string)

def fun2():
    # 读取摘要内容
    descs = soup.find_all(class_="postCon")
    # descs = soup.find_all(class_="c_b_p_desc")
    for i in descs:
        # tag的.contents 属性可以将tag的子节点以列表的方式输出
        c = i.div.contents[0]   #读取第一个
        print(c)

def fun3():
    times = soup.find_all(class_="dayTitle")
    title = soup.find_all(class_="postTitle")
    descs = soup.find_all(class_="postCon")
    # read = soup.find_all(class_= "c_b_p_desc_readmore")
    for i,j,k in zip(times, title, descs):
    # for i,j,k,l in zip(times, title, descs, read):        
        print(i.a.string)
        print(j.a.string)
        print(k.div.contents[0])
        # print(l.a.string)
        # print(l.div.contents[0])        
        print("********")
    
    # tag_soup = soup.find(class_="c_b_p_desc")
    # print (len(tag_soup.contents))
    # for I in tag_soup.contents:
    #     print(I)


fun3()

