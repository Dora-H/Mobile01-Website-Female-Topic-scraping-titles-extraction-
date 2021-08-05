Mobile01 Website  Female-Topics scraping, titles extraction.

## Requirements
● Python 3    
● requests   
● lxml   
● queue
● threading
● time


## Class
MfSpider


## Functions
● getUrl    
● getHtml  
● getContext  
● Work


## Run Codes
### Simply Crawling and Scraping Web Pages with below descriptions to start:

#### 1. Call the main finction to work, Work.
    if __name__=="__main__":
    #整體程序開始執行時間
    begin_time = time.time()
    spider = MfSpider()
    spider.Work()
    end_time = time.time()
    print('總程序執行時間: ',end_time - begin_time)
				
#### 2. Go to the first function, getUrl:
    
				
#### 3. Go to the getHtml function:
    	
    
#### 4. Go to the getContext function:
    
        
#### 5. Finish:
	
    
## Simply Crawling and Scraping Web Pages with setting s & e:
        def getUrl(self):
        for pgNum in range(s,e):
        
            s >> the page number to start
            e >> the end page number 
            
            url = self.baseurl + '&p=' + str(pgNum)
            self.urlsQ.put(url)
