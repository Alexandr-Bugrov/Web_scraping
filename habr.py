import re
from general_functions import get_soup
from decorator import Logger

class Habr():
    def __init__(self, KEYWORDS, HEADERS):
        self.base_url = 'https://habr.com'
        self.KEYWORDS = KEYWORDS
        self.HEADERS = HEADERS

    def get_new_articles(self):
        article = get_soup(self.base_url).find_all('article')
        return article

    def get_article_text(self, url):
        soup = get_soup(url)
        body = soup.find(xmlns='http://www.w3.org/1999/xhtml').text
        return body

    @Logger('logger.log')
    def find_articles(self):
        articles = self.get_new_articles()
        for article in articles:
            article_title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            article_title_match = re.findall(f"{'|'.join(self.KEYWORDS)}", article_title)
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            hubs = article.find_all(class_='tm-article-snippet__hubs-item')
            hubs = [hub.text for hub in hubs]
            keys = ' '.join(hubs).split(' ')
            hubs_match = set(keys) & set(self.KEYWORDS)
            article_text = self.get_article_text(f'{self.base_url}{href}')
            article_text_match = re.findall(f"{'|'.join(self.KEYWORDS)}", article_text)
            if hubs_match != set() or article_title_match != [] or article_text_match != []:
                time_published = article.find('time').text
                print(f'{time_published} - {article_title} - {self.base_url}{href}')