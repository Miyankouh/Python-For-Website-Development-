import json

import requests
from abc import ABC, abstractmethod
from config import BASE_LINK
from bs4 import BeautifulSoup

from parser import AdvertisementPageParser


class CrawlerBase(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def store(self, data):
        pass

    @staticmethod
    def get(link):
        try:
            response = requests.get(link)
        except requests.HTTPError:
            return None
        return response




class LinkCrawler(CrawlerBase):

    def __init__(self, cities, link=BASE_LINK):
        self.cities = cities
        self.link = link

    def find_links(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup.find_all('a', attrs={'class': 'hdrlnk'})

    def start_crawl_city(self, url):
        start = 0
        crawl = True
        adv_links = list()
        while crawl:
            response = self.get(url + start)
            if response is None:
                crawl = False
                continue
            new_links = self.find_links(response.text)
            adv_links.extend(new_links)
            start += 120
            crawl = bool(len(new_links))

        return adv_links

    def start(self):
        adv_links = list()
        for city in self.cities:
            links = self.start_crawl_city(self.link.format(city))
            print(f'{city} total: {len(links)}')
            adv_links.extend(links)
        self.store([li.get('href') for li in adv_links])

    def store(self, data):
        with open('fixtures/data.json', 'w') as f:
            f.write(json.dumps(data))


class DataCrawler(CrawlerBase):

    def __init__(self):
        self.links = self.__load_links()
        self.parser = AdvertisementPageParser()
    
    @staticmethod
    def __load_links():
        with open('fixtures/data.json', 'r') as f:
            links = json.loads(f.read())
        return links

    def start(self):
        for link in self.links:
            response = self.get(link)
            data = self.parser.parse(response.text)
            print(data)

    def store(self, data):
        with open('fixtures/data.json', 'w') as f:
            f.write(json.dumps(data))
