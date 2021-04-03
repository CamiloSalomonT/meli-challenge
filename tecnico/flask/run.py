import logging
from flask import Flask
from flask_restx import Api

import app.common.configuration as config
from app.resources.pipeline import Pipeline


logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] - %(threadName)-10s : %(message)s")

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)


# Application modules
api.add_resource(Pipeline, "/pipeline")


if __name__ == "__main__":
    app.run(host=config.asString("Application", "host"), port=config.asInteger("Application", "port"), debug=True, use_reloader=False)
