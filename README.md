Mobile01 Website  Female-Topics scraping, titles extraction.


## Requirements
● Python 3    
● requests   
● lxml   
● queue  
● threading    
● time   


## Class
MfSpyder


## Functions
● getUrl    
● getHtml  
● getContext  
● Work


## Run Codes
### Simply Crawling and Scraping Web Pages with below descriptions to start:

#### 0. Call the main finction to work. (& Record the execution time of code program.)
    if __name__=="__main__":
       # to activate a time period record.
       begin_time = time.time()
       
       spyder = MfSpyder()
       # call spyder to work.
       spyder.Work()
       
#### 1. Go to the Work function:   
    # Main 
    def Work(self):
        #先設定一個籃子放置 所有urls組合
        thread_basket = []
        #啟動獲取urls組合
        self.getUrl()
        # creat three getHtml threadings
        for t in range(3):
            threeRes = threading.Thread(target = self.getHtml)
            # to put in the basket
            thread_basket.append(threeRes)
           
        # creat two getContext threadings
        for t in range(2):
            twoParse = threading.Thread(target = self.getContext)
            #to put in the basket
            thread_basket.append(twoParse)
           
        #讓所有線程都出動
        for ppl in thread_basket:
            ppl.setDaemon(True)
            ppl.start()
       
        #如果組合為空，則執行其他程序
        self.urlsQ.join()
        self.ressQ.join()

#### 2. Go to the getUrl function:
    #生成urls網址組合
    def getUrl(self):
    #指定要爬取幾頁，依照網址規律設定，此為第1頁至第15頁
       for pgNum in range(1,16):
          url = self.baseurl + '&p=' + str(pgNum)
          #將之依序放(put)urls網址組合中
          self.urlsQ.put(url)
				
#### 3. Go to the getHtml function:
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
           
    
#### 4. Go to the getContext function:
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
        
#### 5. Finish:
       # to end the time period record.
       end_time = time.time()
       # prints the execution time
       print('Codes execution time: ', end_time - begin_time)
