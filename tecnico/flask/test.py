import unittest

import app.common.configuration as config

from app.data.interpreter_manager import InterpreterManager

from app.data.interpreter.csv_interpreter import CsvInterpreter
from app.data.interpreter.json_interpreter import JsonInterpreter


class TestInterpreter(unittest.TestCase):

    scope = "Testing"
    manager = InterpreterManager()

    def test_interpreter_csv(self):
        filepath = config.asString(self.scope, "filepath_csv")
        clazz = interpreter = self.manager.get_interpreter(filepath).__class__
        self.assertEqual(clazz, CsvInterpreter)

    def test_interpreter_json(self):
        filepath = config.asString(self.scope, "filepath_json")
        clazz = interpreter = self.manager.get_interpreter(filepath).__class__
        self.assertEqual(clazz, JsonInterpreter)

    def test_interpreter_no_format(self):
        filepath = config.asString(self.scope, "filepath_garbage")
        with self.assertRaises(Exception):
            clazz = interpreter = self.manager.get_interpreter(filepath).__class__


if __name__ == "__main__":
    unittest.main()
