from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.common.configuration as config
import app.data.database.dbmodels as Models

db_string = "{protocol}://{username}:{password}@{host}:{port}/{database}"

DB_SCOPE = "Database"
HOST = config.asString(DB_SCOPE, "host")
PORT = config.asString(DB_SCOPE, "port")
PROTOCOL = config.asString(DB_SCOPE, "protocol")
USERNAME = config.asString(DB_SCOPE, "username")
PASSWORD = config.asString(DB_SCOPE, "password")
DATABASE = config.asString(DB_SCOPE, "database")

db = create_engine(db_string.format(protocol=PROTOCOL, username=USERNAME, password=PASSWORD, host=HOST, port=PORT, database=DATABASE))

Session = sessionmaker(db)

Models.Base.metadata.create_all(db)


def save_all(articles: List[Models.ArticleModel]):
    session = Session()
    for art in articles:
        session.merge(art)
    session.commit()
