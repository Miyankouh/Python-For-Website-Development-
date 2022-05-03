import requests
from bs4 import BeautifulSoup


def crawl_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        header_div = soup.find('div', attrs={'class': 'news-detail-header'})
        title = header_div.find('h1')
        print(title.text)


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


if __name__ == "__main__":
    # links = [
    #     'https://www.trthaber.com/haber/spor/fenerbahce-beko-rusyada-farkli-kazandi-551690.html',
    #     'https://www.trthaber.com/haber/spor/bright-osayi-samuel-ilk-kez-takimla-antrenmana-cikti-551726.html',
    #     'https://www.trthaber.com/haber/spor/galatasaray-mustafa-muhammedin-transferinde-sona-geldi-551713.html',
    #     'https://www.trthaber.com/haber/spor/eskisehirspor-transfer-yasagi-sorununu-cozemedi-551694.html',
    # ]
    #
    # for link in links:
    #     crawl_page(link)

    get_links()