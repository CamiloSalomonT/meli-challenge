import re
from typing import Optional

from app.data.dto import Article
from app.data.interpreter.interpreter import DataInterpreter
import app.common.configuration as config


class CsvInterpreter(DataInterpreter):
    def __init__(self):
        SCOPE = "CSV"
        self.delimiter = config.asString(SCOPE, "delimiter")
        self.idx_id = config.asInteger(SCOPE, "idx_id")
        self.idx_site = config.asInteger(SCOPE, "idx_site")

    def verify(self, filepath) -> Optional[bool]:
        with open(filepath, "r") as f:
            sample1 = f.readline().strip()  # Possibly titles
            sample2 = f.readline().strip()
        attrs_2 = sample2.split(self.delimiter)

        if len(attrs_2) < 2:
            return False

        ID_PATTERN = "\\d+"
        id = attrs_2[self.idx_id]
        id_check = re.match(ID_PATTERN, id)

        site = attrs_2[self.idx_site]
        SITE_PATTERN = "[a-zA-Z]{3}"
        site_check = re.match(SITE_PATTERN, site)

        same_len_check = len(sample1.split(self.delimiter)) == len(attrs_2)

        return id_check and site_check and same_len_check

    def interpret(self, line: str) -> Optional[Article]:
        data = line.strip().split(self.delimiter)

        ID_PATTERN = "\\d+"
        id = data[self.idx_id]
        id_check = re.match(ID_PATTERN, id)

        if not id_check:
            return None

        return Article(data[self.idx_site], data[self.idx_id])
