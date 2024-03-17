from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fructose import Fructose
from pandas import DataFrame
from dataclasses import dataclass
from finscraper.spiders import YLEArticle

ai = Fructose()

spider = YLEArticle().scrape(10)

def get_articles() -> list:
    return spider.get('list')


@dataclass
class Article:
    title: str
    body: str

@ai()
def generate_article_from_examples(articles: list) -> Article:
    """
    Return a new article inspired by the user provider source articles. Make it outlandish.
    """

@ai(debug=True)
def format_article_response(article: Article) -> str:
    """
    Format the given article into HTML and return it as a string. Use appropriate tags for title, paragraphs and other text styles.
    """

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_index():
    articles = get_articles()
    article = generate_article_from_examples(articles)
    html = format_article_response(article)
    return html

