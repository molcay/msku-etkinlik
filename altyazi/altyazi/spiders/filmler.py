# -*- coding: utf-8 -*-
import scrapy


class FilmlerSpider(scrapy.Spider):
    name = "filmler"
    allowed_domains = ["www.turkcealtyazi.org"]
    start_urls = ['http://www.turkcealtyazi.org/filtre.php?yil=2014&sira=1&tip=1']
    page = 1

    def parse(self, response):
    	links = response.css("td.rowbeyaz:nth-child(2) a::attr(href)").extract()
    	for l in links:
    		l = response.urljoin(l)
    		yield scrapy.Request(l, callback=self.parse_film)
    	if len(links) > 0:	
	    	next_page_url = self.start_urls[0]
	    	self.page += 1
	    	if self.page==8: return
	    	next_page_url += "&p=" + str(self.page)	
	    	yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_film(self,response):
        title = response.css("h1 span:first-child::text").extract_first()    		
        yield {
          "title": title
        }  
        divs = response.css(".altsonsez2")
        for d in divs:
            flag = d.css(".aldil span::attr(class)").extract_first()
            if flag == "flagen":
                l = d.css(".alisim a::attr(href)").extract_first()
                l = response.urljoin(l)
                yield scrapy.Request(l, callback=self.parse_subtitle)
    
    def parse_subtitle(self,response):
    	 description = response.css(".sub-right-container:nth-child(8)::text").extract_first()

    	 form = response.css(".nblock form")
    	 payload = {}
    	 payload["idid"] = form.css("input:nth-child(1)::attr(value)").extract_first()
    	 payload["altid"] = form.css("input:nth-child(2)::attr(value)").extract_first()
    	 payload["sidid"] = form.css("input:nth-child(3)::attr(value)").extract_first()

    	 yield payload
    	 url = "http://www.turkcealtyazi.org/down.php"
    	 yield scrapy.FormRequest(url=url,
    	            formdata=payload,
    	            callback=self.download_file)

    def download_file(self,response):
    	header = str(response.headers["Content-Disposition"])
    	header = header.split("=")[1]
    	yield { 
    	  "filename": header
        }

        
