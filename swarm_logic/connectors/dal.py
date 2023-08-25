from typing import Iterable
from base import DatabaseConnector
import opendal



class OpenDALConnector(DatabaseConnector):

    def __init__(self, scheme, **kwargs):
        self.op = opendal.Operator(scheme, **kwargs)

    def read(self, path: str) -> bytes:
        return self.op.read(path)

    def write(self, path: str, bs: bytes):
        self.op.write(path, bs)

    def stat(self, path: str) -> opendal.Metadata:
        return self.op.stat(path)

    def create_dir(self, path: str):
        self.op.create_dir(path)

    def delete(self, path: str):
        self.op.delete(path)

    def list(self, path: str) -> Iterable[opendal.Entry]:
        return self.op.list(path)

    def scan(self, path: str) -> Iterable[opendal.Entry]:
        return self.op.scan(path)