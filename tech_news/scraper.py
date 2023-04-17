import time
import requests
from requests import HTTPError, Timeout
from parsel import Selector
from bs4 import BeautifulSoup


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


def clean_string_ending(string):
    stripped_string = string.split("\xa0")[0].rstrip(". ")
    return stripped_string


def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def extract_reading_time(reading_time):
    html = reading_time.split(" ")
    time = [int(char) for char in html if char.isdigit()]
    return int(time[0])


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author > a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    summary = selector.css("div.entry-content > p").getall()[0]
    category = selector.css("a.category-style > span.label::text").get()
    summary_without_tags = strip_html_tags(summary).strip().replace("\n", " ")

    return {
        "url": clean_string_ending(url),
        "title": clean_string_ending(title),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": extract_reading_time(reading_time),
        "summary": summary_without_tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
