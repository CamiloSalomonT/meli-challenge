import json
from typing import Optional

from app.data.dto import Article
from app.data.interpreter.interpreter import DataInterpreter
import app.common.configuration as config


class JsonInterpreter(DataInterpreter):
    def __init__(self):
        SCOPE = "JSON"
        self.idx_id = config.asString(SCOPE, "attrname_id")
        self.idx_site = config.asString(SCOPE, "attrname_site")

    def verify(self, filepath) -> bool:
        with open(filepath, "r") as f:
            sample = f.readline().strip()
        try:
            json.loads(sample)
        except:
            return False
        return True

    def interpret(self, line) -> Optional[Article]:
        return json.loads(line)