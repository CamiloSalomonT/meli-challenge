import app.common.configuration as conf
from itertools import islice


SCOPE = "IO"
CONFIG_CHUNK_SIZE = conf.asInteger(SCOPE, "chunk_size")
CONFIG_ENCONDING = conf.asString(SCOPE, "encoding")


def read_chunks(filename, chunk_size=CONFIG_CHUNK_SIZE):
    with open(filename, "r", encoding=CONFIG_ENCONDING) as f:
        for lines in iter(lambda: tuple(islice(f, chunk_size)), ()):
            yield lines


def read_lines(stream, chunk_size):
    for lines in iter(lambda: tuple(islice(stream, chunk_size)), ()):
        yield lines