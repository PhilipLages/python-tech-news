import time
import requests

# Requisito 1
def fetch(url):
    header = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        data = requests.get(url, headers=header, timeout=3)
        data.raise_for_status()
        return data.text
    except:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
