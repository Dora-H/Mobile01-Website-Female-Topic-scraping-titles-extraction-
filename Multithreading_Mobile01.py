'''多線程-Mobile01網站/ 女性 / 光鮮亮麗玩保養'''
import requests
from lxml import etree
from queue import Queue
import threading
import time

class MfSpider(object):
    def __init__(self):
        self.baseurl = "https://www.mobile01.com/topiclist.php?f=372"
        self.headers = {'User-Agent':'Morzilla/5.0'}
        #urls網址組合
        self.urlsQ = Queue()
        #響應組合
        self.ressQ = Queue()
   
    #生成urls網址組合
    def getUrl(self):
        #指定要爬取幾頁，依照網址規律設定，此為第1頁至第15頁
        for pgNum in range(1,16):
            url = self.baseurl + '&p=' + str(pgNum)
            #將之依序放(put)urls網址組合中
            self.urlsQ.put(url)
   
    #獲得網址原始碼組合
    def getHtml(self):
        #設定從self.urlsQ網址組合中循環提取url
        while True:
            #提取
            url = self.urlsQ.get()
            response = requests.get(url,headers=self.headers)
            response.encoding = 'utf-8'
            html = response.text
            #將之依序放(put)響應組合中
            self.ressQ.put(html)
            #從self.urlsQ網址組合中提取url後需要刪除(task_done())
            self.urlsQ.task_done()
           
    #解析原始碼
    def getContext(self):
        while True:
            #依序獲得網址原始碼組合中獲取
            html = self.ressQ.get()
            parseHtml = etree.HTML(html)
            r_list = parseHtml.xpath('//div[@class="l-listTable__tbody"]//div[@class="c-listTableTd__title"]//a[@class]')
            for r in r_list:
                print(r.text)
                               
            #從self.ressQ網址組合中提取html後需要刪除(task_done())
            self.ressQ.task_done()
           
           
    #主要運作按鈕
    def Work(self):
        #先設定一個籃子放置 所有urls組合
        thread_basket = []
        #啟動獲取urls組合
        self.getUrl()
        #創建3個getHtml線程
        for t in range(3):
            threeRes = threading.Thread(target = self.getHtml)
            #將之放進籃子中
            thread_basket.append(threeRes)
           
        #創建2個getContext線程
        for t in range(2):
            twoParse = threading.Thread(target = self.getContext)
            #也將之放進籃子中
            thread_basket.append(twoParse)
           
        #讓所有線程都出動
        for ppl in thread_basket:
            ppl.setDaemon(True)
            ppl.start()
       
        #如果組合為空，則執行其他程序
        self.urlsQ.join()
        self.ressQ.join()
           
   
   
if __name__=="__main__":
    #整體程序開始執行時間
    begin_time = time.time()
    spider = MfSpider()
    spider.Work()
    end_time = time.time()
    print('總程序執行時間: ',end_time - begin_time)
