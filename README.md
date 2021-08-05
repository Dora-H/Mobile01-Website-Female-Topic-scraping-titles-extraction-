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

#### 1. Call the main finction to work, Work. (& Record the execution time of code program.)
    if __name__=="__main__":
       # to activate a time period record.
       begin_time = time.time()
       
       spyder = MfSpider()
       # call s
       spyder.Work()
       				
#### 2. Go to the first function, getUrl:
    
				
#### 3. Go to the getHtml function:
    	
    
#### 4. Go to the getContext function:
    
        
#### 5. Finish:
       # to end the time period record.
       end_time = time.time()
       # prints the execution time
       print('Codes execution time: ', end_time - begin_time)
    
## Simply Crawling and Scraping Web Pages with setting s & e:
        def getUrl(self):
        for pgNum in range(s,e):
        
            s >> the page number to start
            e >> the end page number 
            
            url = self.baseurl + '&p=' + str(pgNum)
            self.urlsQ.put(url)
