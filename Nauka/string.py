#!/usr/bin/env python3
#bundlescraper
#print("Hello World")

import requests
from bs4 import BeautifulSoup

url="https://www.humblebundle.com/software/computer-care-software"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

#bundle tiers
# dd-header-headline
#wyszukiwanie i listowanie nagłówków ze wskazanym stylem
tier_headlines = soup.select(".dd-header-headline")
# for tier in tier_headlines:
#     print(tier.text.strip())

#tablica z naglowkami
#stripped_tiernames = [tier.text.strip() for tier in tier_headlines]

#wersja skrocona:

stripped_tiernames = [tier.text.strip() for tier in tier_headlines]

#lista produktow z konkretnych przedzialow cenowych (tiers)

tiers = {
    "tier1": {
        "price": 500,
        "products": [
            "name1",
            "name2"
        ]
    },
    "tier2": {
        "price": 600,
        "products": [
            "name1",
            "name2"
        ]
    }
}

