import logging
import unittest

import app.common.configuration as config

from app.data.interpreter_manager import InterpreterManager

from app.data.interpreter.csv_interpreter import CsvInterpreter
from app.data.interpreter.json_interpreter import JsonInterpreter


class TestInterpreter(unittest.TestCase):

    scope = "Testing"
    manager = InterpreterManager()

    def test_interpreter_csv(self):
        print("-  Testing Interpreter Manager for CSV format")
        filepath = config.asString(self.scope, "filepath_csv")
        clazz = interpreter = self.manager.get_interpreter_by_filepath(filepath).__class__
        self.assertEqual(clazz, CsvInterpreter)

    def test_interpreter_json(self):
        print("-  Testing Interpreter Manager for JSON format")
        filepath = config.asString(self.scope, "filepath_json")
        clazz = interpreter = self.manager.get_interpreter_by_filepath(filepath).__class__
        self.assertEqual(clazz, JsonInterpreter)

    def test_interpreter_no_format(self):
        print("-  Testing Interpreter Manager for Unknown format")
        filepath = config.asString(self.scope, "filepath_garbage")
        with self.assertRaises(Exception):
            clazz = interpreter = self.manager.get_interpreter_by_filepath(filepath).__class__


if __name__ == "__main__":
    unittest.main()
