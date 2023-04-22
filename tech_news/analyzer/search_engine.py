from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news_info = []

    query = {"title": {"$regex": title, "$options": "i"}}

    for info in search_news(query):
        if title.lower() in info["title"].lower():
            news_info.append((info["title"], info["url"]))

    return news_info


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
