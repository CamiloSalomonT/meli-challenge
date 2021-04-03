from typing import List

import app.control.api_calls as Api
import app.data.file_reader as FileReader
import app.data.database.database as db

from app.data.dto import Article
from app.data.interpreter_manager import InterpreterManager
import app.data.cache as Cache


CURRENCIES = None


def get_currency_name(currency_id):
    """Due to the low dispersion of the currencies, we used a dict to caching them.

    Args:
        currency_id (str): The currency's identifier, e.g., "USD"

    Returns:
        str: The currency's name
    """
    global CURRENCIES
    if not CURRENCIES:
        CURRENCIES = Api.get_currencies()
    return CURRENCIES.get(currency_id)


def complete_articles_info(articles: List[Article]) -> List[Article]:
    """Method to complete all article requiered information.

    Args:
        articles (List[Article]): Articles to be completed

    Returns:
        List[Article]: Articles completed
    """
    articles = Api.call_items(articles)
    # Based on the information we infer which articles are not on the database
    articles = list(filter(lambda art: art._seller_id, articles))
    articles = Api.call_users(articles)

    arts_wo_category = []

    for article in articles:
        article.currency = get_currency_name(article._currency_id)

        if article._category_id:
            if cat := Cache.get(article._category_id):
                article.category = cat
            else:
                arts_wo_category.append(article)

    arts_w_category = Api.call_categories(arts_wo_category)

    for article in arts_w_category:
        if article.category and article._category_id:
            Cache.set(article._category_id, article.category)

    return articles


def call_pipeline(filename: str):
    """The main method of the challenge. This run the pipeline over the given file

    Args:
        filename (str): [description]
    """
    interpreter_man = InterpreterManager()
    interpreter = interpreter_man.get_interpreter(filename)

    for chunk in FileReader.read_chunks(filename):
        articles = []
        for line in chunk:
            if art := interpreter.interpret(line):
                articles.append(art)

        articles = complete_articles_info(articles)

        art_models = []
        for article in articles:
            art_models.append(article.obtainModel())

        db.save_all(art_models)