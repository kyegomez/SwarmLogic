from abc import ABC, abstractmethod
from typing import Iterable


class DatabaseConnector(ABC):

    @abstractmethod
    def read(self, path: str) -> bytes:
        pass

    @abstractmethod
    def write(self, path: str, bs: bytes):
        pass

    @abstractmethod
    def stat(self, path: str) -> opendal.Metadata:
        pass

    @abstractmethod
    def create_dir(self, path: str):
        pass

    @abstractmethod
    def delete(self, path: str):
        pass

    @abstractmethod
    def list(self, path: str) -> Iterable[opendal.Entry]:
        pass

    @abstractmethod
    def scan(self, path: str) -> Iterable[opendal.Entry]:
        pass

    
