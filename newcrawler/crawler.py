from models import Article
from bs4 import BeautifulSoup
import requests


def crawl_page(url):
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        header_div = soup.find('div', attrs={'class': 'news-detail-header'})
        title = header_div.find('h1')
        body = soup.select_one('.detYazi')
        return {'body': body.text, 'title': title.text}
    return {'body':'' , 'title': ''}


def get_links():
    response = requests.get('https://www.trthaber.com/haber/spor/')
    links = list()
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.attrs.get('href')
            if href is not None and href.startswith('haber/spor'):
                links.append('https://www.trthaber.com/' + href)

    return links
