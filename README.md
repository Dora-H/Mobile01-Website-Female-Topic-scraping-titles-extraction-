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
        # create a basket for putting all urls
        thread_basket = []
	
        # activate getUrl function, go to step 2
        self.getUrl()
	
        # creat three getHtml threadings
        for t in range(3):
            # activate getHtml function, go to step 3		
            threeRes = threading.Thread(target = self.getHtml)
	    
            # to put in the basket
            thread_basket.append(threeRes)
           
        # creat two getContext threadings
        for t in range(2):
	    # activate getContext function, go to step 4
            twoParse = threading.Thread(target = self.getContext)
	    
            # to put in the basket
            thread_basket.append(twoParse)
           
        # activate all threadings
        for ppl in thread_basket:
            ppl.setDaemon(True)
            ppl.start()
       
        # if it is empty, run other functions
        self.urlsQ.join()
        self.ressQ.join()

#### 2. Go to the getUrl function:
    def getUrl(self):
    # specify the numbers of web page to crawle, this code is from page1-15
       for pgNum in range(1,16):
          url = self.baseurl + '&p=' + str(pgNum)
	  
          # put urls in urlsQ in ordered to quene
          self.urlsQ.put(url)
	  
	  # go back to step 1 line 46
				
#### 3. Go to the getHtml function:
    def getHtml(self):
        while True:
            # extract urls from urlsQ function in ordered
            url = self.urlsQ.get()
            response = requests.get(url,headers=self.headers)
            response.encoding = 'utf-8'
            html = response.text
	    
            # then put htmls into ressQ function
            self.ressQ.put(html)
	    
            # delete a task after is deing done from urlsQ function by using task.done()
            self.urlsQ.task_done()
           
	    # go back to step 1 line 53
    
#### 4. Go to the getContext function:
    def getContext(self):
        while True:
            # extract html from ressQ function in ordered
            html = self.ressQ.get()
            parseHtml = etree.HTML(html)
            r_list = parseHtml.xpath('//div[@class="l-listTable__tbody"]//div[@class="c-listTableTd__title"]//a[@class]')
            for r in r_list:
                print(r.text)
                               
            #delete a task after is deing done from ressQ function by using task.done()
            self.ressQ.task_done()
        
#### 5. Finish:
       # to end the time period record.
       end_time = time.time()
       
       # prints the execution time
       print('Codes execution time: ', end_time - begin_time)
