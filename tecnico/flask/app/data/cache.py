import redis

import app.common.configuration as config

CACHE_SCOPE = "Cache"
HOST = config.asString(CACHE_SCOPE, "host")
PORT = config.asInteger(CACHE_SCOPE, "port")

__cache_engine__ = redis.Redis(host=HOST, port=PORT, decode_responses=True)


def get(id: str):
    return __cache_engine__.get(id)


def set(id: str, value: str):
    return __cache_engine__.set(id, value)
