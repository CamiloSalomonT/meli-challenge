import os
from os.path import dirname

# This may seem like a magic trick, but it allows to avoid the boilerplate in this file. Otherwise, we would have to import manually each of the implemented interpreters
modules =filter(lambda f: f.endswith(".py") and not f.endswith('__init__.py') and not f.endswith('\\interpreter.py'), os.listdir(dirname(__file__)))
__all__ = list(map(lambda f: f[:-3], modules))