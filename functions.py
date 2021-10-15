import numpy as np
import requests
from bs4 import BeautifulSoup as BS

def goodfood(ingredient):
    search_term = ingredient.replace(' ','+')
    url='https://www.bbcgoodfood.com/search/recipes/?q='+search_term+'&sort=-popular'
    soup = BS(requests.get(url).text)
    results = soup.find_all("a",class_="standard-card-new__article-title qa-card-link")
    hrefs = [x['href'] for x in results]
    choice = hrefs[np.random.randint(low=0,high=len(hrefs))]
    return_url = "https://www.bbcgoodfood.com"+choice
    return return_url

def bonappetit(ingredient):
    search_term = ingredient.replace(' ','%20')
    url = 'https://www.bonappetit.com/search/'+search_term+'?content=recipe&sort=highestRated'
    soup = BS(requests.get(url).text)
    results = soup.find_all("a",class_="photo-link")
    hrefs = [x['href'] for x in results]
    choice = hrefs[np.random.randint(low=0,high=len(hrefs))]
    return_url = "https://bonappetit.com"+choice
    return return_url

def nigella(ingredient):
    search_term = ingredient.replace(' ','+')
    url = 'https://www.nigella.com/recipes/search?term='+search_term+'&occasion=&theme='
    soup = BS(requests.get(url).text)
    results = soup.find_all("a")[27:38]
    hrefs = [x['href'] for x in results]
    choice = hrefs[np.random.randint(low=0,high=len(hrefs))]
    return_url = "https://www.nigella.com"+choice
    return return_url

def olive(ingredient):
    search_term = ingredient.replace(' ','+')
    url = 'https://www.olivemagazine.com/search/recipes/?q='+search_term
    soup = BS(requests.get(url).text)
    results = soup.find_all("a",class_="img-container img-container--portrait-thumbnail")
    hrefs = [x['href'] for x in results]
    choice = hrefs[np.random.randint(low=0,high=len(hrefs))]
    return_url = 'https://www.olivemagazine.com'+choice
    return return_url

func_dict = {'BBC Good Food':goodfood, 'Bon Appetit':bonappetit, 'Nigella':nigella, 'Olive':olive}
