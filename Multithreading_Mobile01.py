import requests
from lxml import etree
from queue import Queue
import threading
import time


class MfSpyder(object):
    def __init__(self):
        self.baseurl = "https://www.mobile01.com/topiclist.php?f=372"
        self.headers = {'User-Agent':'Morzilla/5.0'}
        #urls網址組合
        self.urlsQ = Queue()
        #響應組合
        self.ressQ = Queue()
   

    def getUrl(self):
        for pgNum in range(1,16):
            url = self.baseurl + '&p=' + str(pgNum)
            self.urlsQ.put(url)
   

    def getHtml(self):
        while True:
            url = self.urlsQ.get()
            response = requests.get(url,headers=self.headers)
            response.encoding = 'utf-8'
            html = response.text
            self.ressQ.put(html)
            self.urlsQ.task_done()
           
        
    def getContext(self):
        while True:
            html = self.ressQ.get()
            parseHtml = etree.HTML(html)
            r_list = parseHtml.xpath('//div[@class="l-listTable__tbody"]//div[@class="c-listTableTd__title"]//a[@class]')
            for r in r_list:
                print(r.text)
                               
            self.ressQ.task_done()
           
           
    def Work(self):
        thread_basket = []
        self.getUrl()
        for t in range(3):
            threeRes = threading.Thread(target = self.getHtml)
            thread_basket.append(threeRes)  
        for t in range(2):
            twoParse = threading.Thread(target = self.getContext)
            thread_basket.append(twoParse)
           
        for ppl in thread_basket:
            ppl.setDaemon(True)
            ppl.start()
       
        self.urlsQ.join()
        self.ressQ.join()
   
   
if __name__=="__main__":
    begin_time = time.time()
    spyder = MfSpyder()
    spyder.Work()
    end_time = time.time()
    print('Codes execution time: ',end_time - begin_time)
