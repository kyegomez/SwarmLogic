from base import DatabaseConnector


class JsonDBConnector(DatabaseConnector):
    def read(self, path: str) -> bytes:
        with open(path, 'r') as f:
            return f.read().encode()
        
    def write(self, path: str, bs: bytes):
        with open(path, 'w') as f:
            f.write(bs.decode())

