import sys 
import requests
from bs4 import BeautifulSoup


def get_page(url, start=0):
    try:
        response = requests.get(url + str(start))
    except:
        return None
    return response
    
    print(response.status_code, response.url)


def find_links(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    # content = soup.find('dive', attrs={'class': 'content'})
    # adv_list = soup.find('li', attes={'class': 'result-row'})
    return soup.find_all('a', attrs={'class': 'hdrlnk'})


def start_crawl_city(url):
    start = 0
    crawl = True
    adv_links = list()
    while crawl:
        response = get_page(url, start)
        if response is None:
            crawl = False
            continue
        new_links = find_links(response.text)
        adv_links.extend(new_links)
        start += 120
        crawl = bool(len(new_links))

    return adv_links
    # for li in links:
        # print(li.get('href'))


def start_crawl():
    cities = ['paris', 'los angeles', 'las vegas', 'new york']
    link ='https://losangeles.craigslist.org/search/hhh?s=0&lang=en&cc=gb'
    for city in cities:
        links = start_crawl_city(link.format(city))
        print(f'{city} total,{ len(links)}')


def get_page_data():
    raise NotImplementedError()


if __name__ == '__main__':
    switch = sys.argv[1]
    if switch == 'find_links':
        start_crawl()
    elif switch == 'exteact_pages':
        get_page_data()
    