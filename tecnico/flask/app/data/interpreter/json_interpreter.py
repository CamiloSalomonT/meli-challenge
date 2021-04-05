import json
from typing import Optional

from app.data.dto import Article
from app.data.interpreter.interpreter import DataInterpreter
import app.common.configuration as conf


class JsonInterpreter(DataInterpreter):
    def __init__(self):
        SCOPE = "JSON"
        self.idx_id = conf.asString(SCOPE, "attrname_id")
        self.idx_site = conf.asString(SCOPE, "attrname_site")

    def verify(self, line) -> bool:
        sample = line.strip()
        try:
            json.loads(sample)
        except:
            return False
        return True

    def interpret(self, line) -> Optional[Article]:
        return json.loads(line)