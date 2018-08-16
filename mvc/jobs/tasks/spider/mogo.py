# -*- coding: utf-8 -*-
from application import app
import  requests
from bs4 import BeautifulSoup
'''
python manager.py runjob -m spider/mogo
'''
class JobTask():
    def __init__(self):
        pass

    def run(self,params):
        for p in range(1,3):
            self.scrapy( p )


    def scrapy(self,p):
        url = "http://www.mgzf.com/list?page={0}".format( p )
        res = requests.get(url=url)
        # app.logger.info( res.text )
        if res.status_code != 200:
            return
        # 用BeautifulSoup获取所需信息
        soup = BeautifulSoup(res.text, "html.parser")

        for item in soup.find_all("div", attrs={'class': 'item-room has-shadow'}):
            # app.logger.info( item.a.getText() )
            tmp_data = []
            tmp_data.append( "[%s]"%(p) + "小区名称：%s" % item.h1.getText().strip().replace("\r\n", ""))
            tmp_data.append( "[%s]"%(p) + "户型：%s" % item.select("h2.text-ellipsis")[0].getText())
            tmp_data.append( "[%s]"%(p) +  "户型描述：%s" % item.select("h2.text-ellipsis")[1].getText())
            tmp_data.append( "[%s]"%(p) + "图片地址：%s" % item.img['src'])
            tmp_data.append( "[%s]"%(p) +  "价格：%s" % item.select(".label-price")[0].getText())
            tmp_data.append( "[%s]"%(p) +  "地理位置：%s" % item.select("p.text-ellipsis")[0].getText())
            app.logger.info("\r\n".join(tmp_data))

