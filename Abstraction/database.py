from abc import ABC,abstractmethod

class DataBase(ABC):
    @abstractmethod
    def connect(self):
        pass

class Mysql(DataBase):
    def connect(self):
        print("Connecting to sql")
    
class PostgreSQL(DataBase):
    def connect(self):
        print("Connecting to postgresql")

class MongoDB(DataBase):
    def connect(self):
        print("Connecting to Mongodb")


db={
    Mysql(),
    PostgreSQL(),
    MongoDB()
}

for db1 in db:
    db1.connect()