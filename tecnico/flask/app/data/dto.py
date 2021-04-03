from app.data.database.dbmodels import ArticleModel


class Article:

    price = None
    start_time = None
    category = None
    currency = None
    seller_nickname = None
    _seller_id = None
    _category_id = None
    _currency_id = None

    def __init__(self, site, id):
        self.site = site
        self.id = id

    def get_identifier(self):
        return self.site + str(self.id)

    def obtainModel(self):
        return ArticleModel(self.site, self.id, self.price, self.start_time, self.category, self.currency, self.seller_nickname)
