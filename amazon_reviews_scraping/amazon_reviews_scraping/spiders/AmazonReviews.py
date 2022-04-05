import scrapy


class AmazonreviewsSpider(scrapy.Spider):
    name = 'AmazonReviews'
    allowed_domains = ["https://www.amazon.com.br/product-reviews/B084DWCZY6/ref=cm_cr_arp_d_viewopt_sr?pageNumber="]
    start_urls = ['https://www.amazon.com.br/product-reviews/B084DWCZY6/ref=cm_cr_arp_d_viewopt_sr?pageNumber=/']

    def parse(self, response):
        pass

class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.com.br']
     
    # Base URL for the World Tech Toys Elite Mini Orion Spy Drone
    myBaseUrl = "https://www.amazon.com.br/product-reviews/B084DWCZY6/ref=cm_cr_arp_d_viewopt_sr?pageNumber="
    start_urls=[]
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,501):
        start_urls.append(myBaseUrl+str(i))
    
    # Defining a Scrapy parser
    def parse(self, response):
            #Get the Review List
            data = response.css('#cm_cr-review_list')
            
            #Get the Review Title
            title = data.css('.review-title')
            
            # Get the Ratings
            star_rating = data.css('.review-rating')
            
            # Get the users Comments
            comments = data.css('.review-text')
            
            date_comments = data.css('.review-date')
            
            count = 0
             
            # combining the results
            for review in star_rating:
                yield{'Title':''.join(title[count].xpath(".//text()").extract()),
                      'Rating': ''.join(review.xpath('.//text()').extract()),
                      'Comment': ''.join(comments[count].xpath(".//text()").extract()),
                      'Date Review': ''.join(date_comments[count].xpath(".//text()").extract())
                     }
                count=count+1    