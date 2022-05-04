import sys
from crawler import crawl_page
from utils.db import create_tables
from crawler import get_links

from models import Article, Category


def crawl_and_get_links():
    cat = Category.create(name='Sport')
    for link in get_links():
        article = Article.create(url=link, category=cat)
        print(article.id)


def crawl_and_scrape_articles():
    articles = Article.select().where(Article.is_completed == False)
    
    for article in articles:
        try:
            data = crawl_page(article.url)
        except:
            article.is_completed = True
            article.save()
        else:
            article.title = data['title']
            article.body = data['body']
            article.is_completed = True
            article.save()


def show_stats():
    articles = Article.select().count()
    categories = Category.select().count()
    completed = Article.select().where(Article.is_completed==True).count()
    print(f"articles: {articles}\t categories: {categories}\t completed: {completed}")


if __name__ == '__main__':

    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'get_links':
        crawl_and_get_links()
    elif sys.argv[1] == 'get_article':
        crawl_and_scrape_articles()
    elif sys.argv[1] == 'stats':
        show_stats()
