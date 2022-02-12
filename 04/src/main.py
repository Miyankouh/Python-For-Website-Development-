import sys
from crawl import LinkCrawler, DataCrawler


if __name__ == '__main__':
    """ You need to go to the Direction file path to exit the terminal """
    switch = sys.argv[1]
    if switch == 'find_links':  # Use for output :> python main.py find_links
        crawler = LinkCrawler(cities=['los angeles', 'new york'])
        crawler.start()
    elif switch == 'extract_pages':
        crawler = DataCrawler()
        crawler.start()