import app.common.configuration as conf
from itertools import islice


SCOPE = "FileReader"
CONFIG_CHUNK_SIZE = conf.asInteger(SCOPE, "chunk_size")
CONFIG_ENCONDING = conf.asString(SCOPE, "encoding")


def read_chunks(filename, chunk_size=CONFIG_CHUNK_SIZE):
    with open(filename, "r", encoding=CONFIG_ENCONDING) as f:
        for n_lines in iter(lambda: tuple(islice(f, chunk_size)), ()):
            yield n_lines
