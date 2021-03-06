# -*- coding: utf-8 -*-


"""
李运辰 2021-3-6

公众号：python爬虫数据分析挖掘
"""
import requests
from lxml import etree

##下载文件
def download(url,title):
    res = requests.get(url)
    res.encoding = 'utf-8'
    text = res.text
    selector = etree.HTML(text)
    href = selector.xpath('//*[@class="download-url"]/a/@href')[0]

    r = requests.get(href)
    with open(str(title)+".rar", "wb") as code:
      code.write(r.content)
    print(str(title)+"：下载完成！")


###遍历每一页
def getlist():

    for k in range(1,501):
        url = "https://sc.chinaz.com/ppt/free_"+str(k)+".html"
        res = requests.get(url)
        res.encoding = 'utf-8'
        text = res.text

        selector = etree.HTML(text)
        list = selector.xpath('//*[@class="bot-div"]')
        for i in list:
            title = i.xpath('.//a/text()')[0].replace("\n", '').replace(" ", '')
            href = i.xpath('.//a/@href')[0].replace("\n", '').replace(" ", '')
            download("https://sc.chinaz.com/"+str(href), str(title))



###开始下载

getlist()



