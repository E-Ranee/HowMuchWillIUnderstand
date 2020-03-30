import requests as r
from bs4 import BeautifulSoup
# calling it by a shorthand

def scrape(url) -> str:
    webpage = r.get(url)
    html = BeautifulSoup(webpage.text, 'html.parser')
    paragraphs = html.article.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text += p.text + "\n\n"

    return article_text

if __name__ == "__main__":
    # Only runs if file run directly ex. python scrape.py
    # if indirectly, if block does not run
    url = "https://elpais.com/internacional/2020-03-28/el-mundo-en-hibernacion-busca-salidas.html"
    print(scrape(url))

    url = "https://elpais.com/internacional/2020-03-28/el-mundo-en-hibernacion-busca-salidas.html"
    print(scrape(url))