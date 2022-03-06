import requests
from bs4 import BeautifulSoup
from redis import Redis

client = Redis()


def get_links(url="https://varzesh3.com"):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text)
    for link in soup.find_all('a'):
        client.rpush('links', link.get('href'))


if __name__ == "__main__":
    get_links()
