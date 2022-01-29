from datetime import datetime
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Table, ForeignKey, Numeric, Boolean
from src.data.setup import Base


class EntityBase(object):
    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))

    def __init__(self) -> None:
        super().__init__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @classmethod
    def get_column_names(cls):
        columns: list[Column]
        columns = cls.get_columns()

        column_names: list[str]
        column_names = [x.name for x in columns]

        return column_names

    @classmethod
    def get_columns(cls: type[Base]):
        table: Table
        table = cls.__getattribute__(cls, '__table__')

        if table is None:
            return []

        columns: list[Column]
        columns = table.columns

        return columns

    def to_dict(self):
        result: dict
        result = {}

        columns: list[Column]
        columns = self.get_columns()

        for column in columns:
            name = column.name
            value = self.__getattribute__(name)
            result[name] = value

        return result

    def from_dict(self, obj: dict):
        for key, value in obj.items():
            if hasattr(self, key):
                setattr(self, key, value)

        return self


class Product(EntityBase, Base):
    __tablename__ = 'products'
    
    name = Column(String)
    type = Column(String)
    description = Column(String)
    material = Column(String)
    price = Column(Numeric)
    available_quantity = Column(Integer)
    status = Column(Boolean) 
