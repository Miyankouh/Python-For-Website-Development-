import sys
from utils.db import create_tables
from crawler import get_links

from models import Article, Category


def run():
    links = get_links()

    cat = Category.create(name='Sport')
    for link in links:
        article = Article.create(url=link, category=cat)
        print(article.id)


if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'run':
        run()
