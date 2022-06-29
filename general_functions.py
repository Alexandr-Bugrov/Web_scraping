import requests
import bs4
from HEADERS import HEADERS
from  decorator import Logger

@Logger('logger.log')
def get_soup(url):
    text = requests.get(url, headers=HEADERS).text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    return soup

@Logger('logger.log')
def keywords_redactor(KEYWORDS:list):
    new_keywords = []
    for keyword in KEYWORDS:
        keyword = keyword.capitalize()
        new_keywords.append(keyword)

    KEYWORDS = KEYWORDS + new_keywords
    return KEYWORDS