# -*- coding: utf-8 -*-
import scrapy
from ..items import Member

class MembersSpider2(scrapy.Spider):
	name = "members2"
	allowed_domains = ["www.europarl.europa.eu"]
	

	def start_requests(self):
		start_url = "http://www.europarl.europa.eu/meps/en/full-list.html?filter={}&leg=".format(self.letter)
		yield scrapy.Request(start_url, self.parse)

	def parse(self, response):
		links = response.css("li.mep_name a::attr(href)").extract()
		for l in links[:5]:
			l = response.urljoin(l)
			yield scrapy.Request(l, callback=self.parse_member)
			print(l)

	def parse_member(self, response):
		name = response.css("li.mep_name a::attr(title)")[0].extract()
		country = response.css("li.nationality::text")[0].extract().strip()
		email = response.css("#email-0::attr(href)").extract_first().strip()
		img_src = response.css("img.photo_mep::attr(src)").extract_first().strip()
		img_src = response.urljoin(img_src)
		member = Member(name=name, country=country, email=email, image_urls=[img_src])

		yield member
		

	
