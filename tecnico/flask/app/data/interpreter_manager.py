from app.data.interpreter.interpreter import DataInterpreter
from app.data.interpreter import *


class InterpreterManager:
    """This class is responsible for engaging the Interpretation Engine and making it easy to use by the application."""

    def __init__(self):
        self.interpreters = []
        for clazz in DataInterpreter.__subclasses__():
            self.interpreters.append(clazz())

    def get_interpreter_by_filepath(self, filepath) -> DataInterpreter:
        with open(filepath, "r") as f:
            f.readline()
            sample = f.readline()
            return self.get_interpreter_by_sample(sample)

    def get_interpreter_by_sample(self, sample) -> DataInterpreter:
        for interpreter in self.interpreters:
            if interpreter.verify(sample):
                return interpreter
        raise Exception(f"It looks that there is no interpreter registered for the sample: {sample}")
