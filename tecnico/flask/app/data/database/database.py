from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.common.configuration as conf
import app.data.database.dbmodels as Models


DB_SCOPE = "Database"
host = conf.asString(DB_SCOPE, "host")
port = conf.asString(DB_SCOPE, "port")
protocol = conf.asString(DB_SCOPE, "protocol")
username = conf.asString(DB_SCOPE, "username")
password = conf.asString(DB_SCOPE, "password")
database = conf.asString(DB_SCOPE, "database")

db_string = f"{protocol}://{username}:{password}@{host}:{port}/{database}"

db = create_engine(db_string)

Session = sessionmaker(db)

Models.Base.metadata.create_all(db)


def save_all(articles: List[Models.ArticleModel]):
    session = Session()
    for art in articles:
        session.merge(art)
    session.commit()
