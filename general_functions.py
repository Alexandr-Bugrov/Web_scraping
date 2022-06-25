import requests
import bs4
from HEADERS import HEADERS

def get_soup(url):
    text = requests.get(url, headers=HEADERS).text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    return soup

def keywords_redactor(KEYWORDS:list):
    new_keywords = []
    for keyword in KEYWORDS:
        keyword = keyword.capitalize()
        new_keywords.append(keyword)
    KEYWORDS = KEYWORDS + new_keywords
    return KEYWORDS