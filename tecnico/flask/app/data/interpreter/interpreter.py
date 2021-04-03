from abc import ABC, abstractmethod
from typing import Optional
from app.data.dto import  Article

class DataInterpreter(ABC):
    """Base interpreter class, with the requiered methods to provide interpretation."""
    
    def __init__(self):
        pass

    @abstractmethod
    def verify(self, filepath) -> bool:
        pass

    @abstractmethod
    def interpret(self, line) -> Optional[Article]:
        pass