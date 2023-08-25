from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker, scoped_session
import opendal

from base import DatabaseConnector

class SQLAlchemyConnector(DatabaseConnector):
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.metadata = MetaData()

    def read(self, path: str) -> bytes:
        #implement read operation
        pass

    def write(self, path: str, bs: bytes):
        #implement sql achemy write operation
        pass

