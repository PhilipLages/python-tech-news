import time
import requests
from requests import HTTPError, Timeout
from parsel import Selector


# Requisito 1
def fetch(url):
    header = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        data = requests.get(url, headers=header, timeout=3)
        data.raise_for_status()
        return data.text
    except (HTTPError, Timeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_urls = selector.css(
        "div.post-outer a.cs-overlay-link::attr(href)"
    ).getall()

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_page_link = selector.css("a.next::attr(href)").get()
        return next_page_link
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
