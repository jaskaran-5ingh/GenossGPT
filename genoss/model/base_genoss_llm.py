from typing import List
from abc import abstractmethod, abstractproperty

from pydantic import BaseModel


class BaseGenossLLM(BaseModel):
    name: str
    description: str
    model_path: str

    @abstractmethod
    def generate_answer(self, prompt: str) -> str:
        print("You need to implement the generate_answer method")
        return "Hello World!"

    @abstractmethod
    def generate_embedding(self, prompt: str) -> List[float]:
        print("You need to implement the generate_embedding method")
        return [0.0, 0.0, 0.0]