# -*- coding: utf-8 -*-
import scrapy


class MembersSpider(scrapy.Spider):
    name = "members"
    allowed_domains = ["www.europarl.europa.eu"]
    start_urls = ['http://www.europarl.europa.eu/meps/en/full-list.html?filter=all&leg=']

    def parse(self, response):
    	links = response.css("li.mep_name a::attr(href)").extract()
    	for l in links:
    		l = response.urljoin(l)
    		yield scrapy.Request(l, callback=self.parse_member)
    		print(l)

    def parse_member(self, response):
    	name = response.css("li.mep_name a::attr(title)")[0].extract()
    	country = response.css("li.nationality::text")[0].extract().strip()
    	email = response.css("#email-0::attr(href)").extract_first().strip()
    	to_replace = [("mailto:", ""), ("[dot]", "."), ("[at]", "@")]
    	for word1, word2 in to_replace:
    		email = email.replace(word1, word2)
    	# email = email.replace("mailto:", "")
    	# email = email.replace("[dot]", ".")
    	# email = email.replace("[at]", "@")
    	email = email[::-1]
    	yield {
    	  "name": name,
    	  "country": country,
    	  "email": email
    	}
    	

    
