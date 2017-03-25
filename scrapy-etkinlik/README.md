# Scrapy Etkinlik 

Bu repo Scrapy etkinliğinde oluşuturulan projeleri, kullanılan GNU/Linux komutlarını içermektedir.

### Repo İçeriği:

* `altyazi`: Üçüncü gün (17 Mart 2017) oluşturulan proje. Bu projede [turkcealtyazi.org](www.turkcealtyazi.org) adresindeki altyazıları çeken bir proje geliştirilmeye çalışıldı.
* `ep_members`: İlk gün (24 Şubat 2017) oluşturulan proje. EP üyelerinin hakkında bilgi edinmek için yazılmış bir spider(__members__)'ı içeren bir proje dizini.
* `ep_members/images`: İkinci gün (3 Mart 2017) yapılan uygulamadaki Resim indirme işinin output dizini.
* `CLI.24Feb.history`: 24 Şubat etkinliğindeki CLI komutlarının geçmişini içeren dosya (`history` command output).
	* `scrapy`: [Scrapy Command Line Tool](https://doc.scrapy.org/en/1.3/topics/commands.html) hakkında detaylı bilgi alma ve parametreleri görüntüleme. 
	* `scrapy startproject ep_members`: **ep_members** isimli bir proje oluşturma.
	* `scrapy shell`**`$URL`**: **$URL** adresine request gönderip dönen sonuç ile özelleştirilmiş bir `Python` interpreter ekranı açılır. [Selector](https://doc.scrapy.org/en/1.3/topics/selectors.html) denemeleri yapabileceğiniz ve Python kodları kullanabileceğiniz bir interpreter. 
	* `scrapy genspider`**`$SPIDER_NAME $ALLOWED_DOMAIN`**: **$SPIDER_NAME** isimli ve **$ALLOWED_DOMAIN** adresi üzerinde tanımlı bir `spider` oluşturmaya yarar.
	* `scrapy crawl`**`$SPIDER_NAME`**: **$SPIDER_NAME** isimli `spider`'ı çalıştırmak için kullanılan komut.
* `CLI.03Mar.history`: 3 Mart etkinliğindeki CLI komutlarının geçmişini içeren dosya (`history` command output).
* `CLI.17.Mar.history`: 17 Mart etkinliğindeki CLI komutlarının geçmişini içeren dosya(`history` command output).
NOT: Scrapy hakkında daha detaylı bilgi almak için [Scrapy](http://scrapy.org/) 'yi zayeret edebilirsiniz.

### Klasör Yapısı ve İçeriği:

```
.
├── altyazi
│   ├── altyazi
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   └── settings.cpython-35.pyc
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── filmler.py
│   │       ├── __init__.py
│   │       └── __pycache__
│   │           ├── filmler.cpython-35.pyc
│   │           └── __init__.cpython-35.pyc
│   ├── data.json
│   └── scrapy.cfg
├── CLI.03Mar.history
├── CLI.17.Mar.history
├── CLI.24Feb.history
├── ep_members
│   ├── css.selector.txt
│   ├── ep_members
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── items.cpython-35.pyc
│   │   │   ├── pipelines.cpython-35.pyc
│   │   │   └── settings.cpython-35.pyc
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── __init__.py
│   │       ├── members2.py
│   │       ├── members.py
│   │       └── __pycache__
│   │           ├── __init__.cpython-35.pyc
│   │           ├── members2.cpython-35.pyc
│   │           └── members.cpython-35.pyc
│   ├── images
│   │   ├── full
│   │   │   ├── 36b292453ed231e9674142a3688fadc98d6fd00a.jpg
│   │   │   ├── 3b6400f24739fa0ec7f366c4ceaa863e09ebedab.jpg
│   │   │   ├── 4fbb78408a0de82092755d83a84f23f8b3f079e3.jpg
│   │   │   ├── 90004054623aa551cfe55783bc17a61a4ec133eb.jpg
│   │   │   └── d57a725c13480ea9d2b4c608ad3d8a7df3a3f610.jpg
│   │   └── thumbs
│   │       └── small
│   │           ├── 36b292453ed231e9674142a3688fadc98d6fd00a.jpg
│   │           ├── 3b6400f24739fa0ec7f366c4ceaa863e09ebedab.jpg
│   │           ├── 4fbb78408a0de82092755d83a84f23f8b3f079e3.jpg
│   │           ├── 90004054623aa551cfe55783bc17a61a4ec133eb.jpg
│   │           └── d57a725c13480ea9d2b4c608ad3d8a7df3a3f610.jpg
│   ├── items.jl
│   ├── items.json
│   ├── members.json
│   └── scrapy.cfg
├── folder_content
└── README.md

14 directories, 48 files
```