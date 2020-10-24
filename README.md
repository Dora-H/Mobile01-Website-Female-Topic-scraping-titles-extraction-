
## Simply Crawling and Scraping Web Pages with setting s & e:
    
    def getUrl(self):
        for pgNum in range(s,e):
        
            s >> the page number to start
            e >> the end page number 
            
            url = self.baseurl + '&p=' + str(pgNum)
            self.urlsQ.put(url)
