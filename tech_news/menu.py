import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category
)


options = {
    0: "Popular o banco com notícias",
    1: "Buscar notícias por título",
    2: "Buscar notícias por data",
    3: "Buscar notícias por categoria",
    4: "Listar top 5 categorias",
    5: "Sair.",
}

user_inputs = {
    0: "Digite quantas notícias serão buscadas:\n",
    1: "Digite o título:\n",
    2: "Digite a data no formato aaaa-mm-dd:\n",
    3: "Digite a categoria:\n",
}


def get_menu_options():
    return "".join(
        [f" {key} - {options[key]};\n" for key in options]
    )


def process_options(option):
    if option == 4:
        return top_5_categories()
    elif option == 5:
        print("Encerrando script\n")
        SystemExit


# Requisitos 11 e 12
def analyzer_menu():
    methods = [
        get_tech_news,
        search_by_title,
        search_by_date,
        search_by_category,
        top_5_categories,
    ]

    try:
        print("Selecione uma das opções a seguir:\n" + get_menu_options())

        option = int(input())
        if option in options and option > 3:
            return process_options(option)

        parameter = input(f"{user_inputs[option]}")
        return methods[option](parameter)

    except (KeyError, ValueError):
        sys.stderr.write("Opção inválida\n")
