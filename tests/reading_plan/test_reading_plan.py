from tech_news.analyzer.reading_plan import ReadingPlanService
from pytest import fixture, raises
from unittest.mock import patch


@fixture
def expected_result():
    return {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        "Não deixe para depois: Python é a"
                        "linguagem mais quente do momento",
                        4,
                    ),
                    (
                        "Selenium, BeautifulSoup ou Parsel?"
                        "Entenda as diferenças",
                        3,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Pytest + Faker: a combinação poderosa dos testes!",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("FastAPI e Flask: frameworks para APIs em Python", 15),
            ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
        ],
    }


def mock():
    return [
        {"title": "Não deixe para depois", "reading_time": 4},
        {"title": "Selenium, BeautifulSoup ou Parsel?", "reading_time": 3},
        {
            "title": "Pytest + Faker: a combinação poderosa dos testes!",
            "reading_time": 10,
        },
        {
            "title": "FastAPI e Flask: frameworks para APIs em Python",
            "reading_time": 15,
        },
        {
            "title": "A biblioteca Pandas e o sucesso da linguagem Python",
            "reading_time": 12,
        },
    ]


def test_reading_plan_group_news(expected_result):
    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mock,
    ):
        result = ReadingPlanService.group_news_for_available_time(10)

        assert result == expected_result

    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        FILE_BASE_PATH = "tech_news.analyzer.reading_plan"
        with patch(
            f"{FILE_BASE_PATH}.ReadingPlanService._db_news_proxy",
            mock,
        ):
            ReadingPlanService.group_news_for_available_time(0)
