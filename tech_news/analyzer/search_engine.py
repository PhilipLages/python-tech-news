from tech_news.database import search_news
from datetime import datetime


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
    try:
        datetime_obj = datetime.strptime(date, "%Y-%m-%d")
        date_str = datetime.strftime(datetime_obj, "%d/%m/%Y")

        news = []
        query = {"timestamp": date_str}
        for info in search_news(query):
            if info.get("timestamp") == date_str:
                news.append((info["title"], info["url"]))

        return news

    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    news_info = []
    query = {"category": {"$regex": category, "$options": "i"}}

    for info in search_news(query):
        if info.get("category", "").lower() == category.lower():
            news_info.append((info["title"], info["url"]))

    return news_info
