from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class ArticleModel(Base):
    __tablename__ = "ARTICLE"

    id = Column(Integer, primary_key=True)
    site = Column(String, primary_key=True)
    price = Column(Float)
    start_time = Column(DateTime)
    category = Column(String)
    currency = Column(String)
    seller_nickname = Column(String)

    def __init__(self, site, id, price, start_time, category, currency, seller_nickname):
        self.site = site
        self.id = id
        self.price = price
        self.start_time = start_time
        self.category = category
        self.currency = currency
        self.seller_nickname = seller_nickname