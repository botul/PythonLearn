import requests

URL = 'https://www.amazon.de/Crucial-MX500-CT500MX500SSD1-Internes-NAND/dp/B0784SLQM6/ref=sr_1_1_sspa?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=mx500&qid=1562960891&s=gateway&sr=8-1-spons&psc=1'

headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, requests)

