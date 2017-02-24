# Scrapy Etkinlik 

Bu repo etkinlikte oluşuturulan projeleri, kullanılan GNU/Linux komutlarını içermektedir.

### Repo İçeriği:

* `ep_members`: İlk gün (24 Şubat 2017) oluşturulan proje. EP üyelerinin hakkında bilgi edinmek için yazılmış bir spider(__members__)'ı içeren bir proje dizini.
* `CLI.24Feb.history`: 24 Şubat etkiliğindeki CLI komutlarının geçmişini içeren dosya (`history` command output).
	* `scrapy`: [Scrapy Command Line Tool](https://doc.scrapy.org/en/1.3/topics/commands.html) hakkında detaylı bilgi alma ve parametreleri görüntüleme. 
	* `scrapy startproject ep_members`: **ep_members** isimli bir proje oluşturma.
	* `scrapy shell`**`$URL`**: **$URL** adresine request gönderip dönen sonuç ile özelleştirilmiş bir `Python` interpreter ekranı açılır. [Selector](https://doc.scrapy.org/en/1.3/topics/selectors.html) denemeleri yapabileceğiniz ve Python kodları kullanabileceğiniz bir interpreter. 
	* `scrapy genspider`**`$SPIDER_NAME $ALLOWED_DOMAIN`**: **$SPIDER_NAME** isimli ve **$ALLOWED_DOMAIN** adresi üzerinde tanımlı bir `spider` oluşturmaya yarar.
	* `scrapy crawl`**`$SPIDER_NAME`**: **$SPIDER_NAME** isimli `spider`'ı çalıştırmak için kullanılan komut.


NOT: Scrapy hakkında daha detaylı bilgi almak için [Scrapy](http://scrapy.org/) 'yi zayeret edebilirsiniz.