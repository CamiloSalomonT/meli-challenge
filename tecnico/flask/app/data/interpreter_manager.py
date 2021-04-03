from app.data.interpreter.interpreter import DataInterpreter
from app.data.interpreter import *


class InterpreterManager:
    """This class is responsible for engaging the Interpretation Engine and making it easy to use by the application."""
    
    def __init__(self):
        self.interpreters = []
        for clazz in DataInterpreter.__subclasses__():
            self.interpreters.append(clazz())

    def get_interpreter(self, filepath) -> DataInterpreter:
        for interpreter in self.interpreters:
            if interpreter.verify(filepath):
                return interpreter
        raise Exception("It looks that there is no interpreter registered for the file: {}".format(filepath))