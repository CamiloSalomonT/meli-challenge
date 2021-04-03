import json
import asyncio
import aiohttp
import logging
import requests

from typing import Callable, Dict, List

from app.data.dto import Article
import app.common.configuration as config


API_SCOPE = "MeliApi"
URL_ITEMS = config.asString(API_SCOPE, "url_base") + config.asString(API_SCOPE, "url_item")
URL_USERS = config.asString(API_SCOPE, "url_base") + config.asString(API_SCOPE, "url_user")
URL_CATEGORIES = config.asString(API_SCOPE, "url_base") + config.asString(API_SCOPE, "url_category")
URL_CURRENCIES = config.asString(API_SCOPE, "url_base") + config.asString(API_SCOPE, "url_currencies")

# BEGIN: Utils for API calls
def get_loop():
    """Sometimes using some threaded libraries may lead to problems get the event loop. This method solves that."""
    try:
        loop = asyncio.get_event_loop()
    except Exception as e:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop


async def get(url: str, article: Article, setter_func: Callable):
    """Used to generalize the async calls, using a setter method to set the attributes for each article"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                rsp = await response.read()
                rsp = json.loads(rsp)
                setter_func(article, rsp)
            else:
                logging.error("{} doesn't exist. Status {} in GET call.".format(article.get_identifier(), response.status))


# END: Utils for API calls


# BEGIN: Data setters from response objects


def set_item(article: Article, dict: Dict):
    article.price = dict.get("price")
    article.start_time = dict.get("start_time")
    article._category_id = dict.get("category_id")
    article._seller_id = dict.get("seller_id")
    article._currency_id = dict.get("currency_id")


def set_seller(article: Article, dict: Dict):
    article.seller_nickname = dict.get("nickname")


def set_categories(article: Article, dict: Dict):
    article.category = dict.get("name")


# END: Data setters from response objects


# BEGIN: API calls to retrieve article's related info


def call_items(articles: List[Article]) -> List[Article]:
    loop = get_loop()
    loop.run_until_complete(asyncio.gather(*[get(URL_ITEMS.format(article.get_identifier()), article, set_item) for article in articles]))
    return articles


def call_users(articles: List[Article]) -> List[Article]:
    loop = get_loop()
    loop.run_until_complete(asyncio.gather(*[get(URL_USERS.format(article._seller_id), article, set_seller) for article in articles]))
    return articles


def call_categories(articles: List[Article]) -> List[Article]:
    loop = get_loop()
    loop.run_until_complete(asyncio.gather(*[get(URL_CATEGORIES.format(article._category_id), article, set_categories) for article in articles]))
    return articles


def get_currencies() -> Dict:
    response = requests.request("GET", URL_CURRENCIES)
    curs = {}
    for currency in json.loads(response.text):
        curs[currency["id"]] = currency["description"]
    return curs


# END: API calls to retrieve article's related info
