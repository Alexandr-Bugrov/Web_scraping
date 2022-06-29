from HEADERS import HEADERS
from KEYWORDS import KEYWORDS
from habr import Habr
from general_functions import keywords_redactor


if __name__ == '__main__':
    habr_site = Habr(keywords_redactor(KEYWORDS), HEADERS)
    habr_site.find_articles()



