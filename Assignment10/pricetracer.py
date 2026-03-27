import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
        self.response = requests.get(self.url, headers=self.headers).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text
        else:
            return "Tag not found"
    def price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Tag not found"

url = input("Enter url: ")
device = PriceTracer(url=url)
print(device.product_title().strip())
print(device.price().strip())