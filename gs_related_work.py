
import sys
import requests
from bs4 import BeautifulSoup

articles = [] # list of articles

# create article class
class Article:
    def __init__(self, title, citation_count, year, related_articles, processed=False):
        self.title = title
        self.citation_count = citation_count
        self.year = year
        self.processed = processed
        self.related_articles = related_articles

    def __str__(self):
        return self.title + ', ' + str(self.year) + ', citation count ' + str(self.citation_count)

    # override the __eq__ method to compare two articles
    def __eq__(self, other):
        return self.title == other.title

# scrape the related articles
# return list of related articles in a JSON format where each article contains the title, year amd the citation count
def scrape_related_articles(url):
    page = requests.get('https://scholar.google.com/' + url)
    soup = BeautifulSoup(page.content, 'html.parser')
    related_articles = soup.find_all('div', class_='gs_ri')
    for article in related_articles:
        article_title = article.find('h3', class_='gs_rt') # get the title of the article

        div_article_info = article.find('div', class_='gs_fl') # get div element with the citation count in the third a child element
        citation_count_str = div_article_info.find_all('a')[2].text # get the citation count string
        citation_count = int(citation_count_str[citation_count_str.rfind(' '):]) # get suffix of the citation count string

        related_articles = div_article_info.find_all('a')[3].get('href') # get the related articles url

        article_year_str = article.find('div', class_='gs_a').text # get the string containing the year of the article before a hyphen
        last_hyphen_position = article_year_str.rfind(' - ') # get the position of the last hyphen
        article_year = int(article_year_str[last_hyphen_position - 4: last_hyphen_position]) # get the year of the article

        article = Article(article_title.a.text, citation_count, article_year, related_articles) # create Article object
        if article not in articles:
            articles.append(article) # append the article object to the list of articles if it is not already in the list

# Search for the publication in scholarly
# def search_publication(publication_title):
#     search_query = scholarly.search_pubs(publication_title)
#     dict_publication = next(search_query) # Get the first result
#     article = Article(publication_title, dict_publication.get('num_citations'), True)
#     if article not in articles:
#         articles.append(article)  # append the article object to the list of articles if it is not already in the list
#     else:
#         a = articles[articles.index(article)]
#         a.processed = True
#     return dict_publication.get('url_related_articles')

def search_related_articles(publication_title, repeat_count=5):
    print("Searching " + publication_title + "\n");
    # replace space with + and search for the publication
    publication_title = publication_title.replace(' ', '+')
    related_articles = "/scholar?hl=cs&as_sdt=0%2C5&q=" + publication_title + "&btnG=&oq="
    for i in range(0, repeat_count):
        scrape_related_articles(related_articles)
        # find first unprocessed article
        article_founded = False
        for article in articles:
            if not article.processed:
                print("Searching " + article.title + "\n");
                related_articles = article.related_articles
                article.processed = True
                article_founded = True
                break
        if not article_founded:
            break


# Check the number of arguments
if len(sys.argv) != 2:
    print("Usage: python gs_related_work.py \"article title\"")
    sys.exit()

# Get the parameter
article_name = sys.argv[1]
search_related_articles(article_name)

# print the related articles sorted according to the citation count
for article in sorted(articles, key=lambda x: x.citation_count, reverse=True):
    print(article)

