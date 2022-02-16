import sys
from crawl2 import LinkCrawler, DataCrawler, ImageDownloader

if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = LinkCrawler(cities=['paris', 'berlin'])
        crawler.start(store=True)

    elif switch == 'extract_pages':
        crawler = DataCrawler()
        crawler.start(store=True)

    elif switch == 'download_images':
        crawler = ImageDownloader()
        crawler.start(store=True)


