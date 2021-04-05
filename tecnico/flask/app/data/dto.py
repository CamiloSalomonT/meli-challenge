from typing import Optional, DateTime
from app.data.database.dbmodels import ArticleModel


class Article:

    price:Optional[float] = None
    start_time:Optional[DateTime] = None
    category:Optional[str] = None
    currency:Optional[str] = None
    seller_nickname:Optional[str] = None
    _seller_id:Optional[str] = None
    _category_id:Optional[str] = None
    _currency_id:Optional[str] = None

    def __init__(self, site, id):
        self.site = site
        self.id = id

    def get_identifier(self):
        return self.site + str(self.id)

    def obtainModel(self):
        return ArticleModel(self.site, self.id, self.price, self.start_time, self.category, self.currency, self.seller_nickname)
