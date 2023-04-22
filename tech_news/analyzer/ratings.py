from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    all_news = find_news()

    category_couter = {}

    for news in all_news:
        category = news.get("category", "")

        if category not in category_couter:
            category_couter[category] = 0

        category_couter[category] += 1

    category_list = list(category_couter.keys())
    category_list.sort(key=lambda c: (-category_couter[c], c))
    top_5_categories = category_list[:5]

    return top_5_categories
