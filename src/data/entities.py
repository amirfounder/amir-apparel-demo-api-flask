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
    demographic = Column(String)
    launch_date = Column(DateTime(True))
    color = Column(String)
    hex_code = Column(String)


class Purchase(EntityBase, Base):
    __tablename__ = 'purchases'

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    shipping_address_street = Column(String)
    shipping_address_street_optional = Column(String)
    shipping_address_city = Column(String)
    shipping_address_state = Column(String)
    shipping_address_zip_code = Column(String)

    billing_address_street = Column(String)
    billing_address_street_optional = Column(String)
    billing_address_city = Column(String)
    billing_address_state = Column(String)
    billing_address_zip_code = Column(String)

    credit_card_cardholder_name = Column(String)
    credit_card_card_number = Column(String)
    credit_card_expiration_date = Column(String)
    credit_card_cvv = Column(String)

    def from_dict(self, obj: dict):
        setattr(self, 'first_name', obj.get('first_name'))
        setattr(self, 'last_name', obj.get('last_name'))
        setattr(self, 'email', obj.get('email'))

        shipping_address = obj.get('shipping_address')
        
        if shipping_address is not None:
            setattr(self, 'shipping_address_street', shipping_address.get('street'))
            setattr(self, 'shipping_address_street_optional', shipping_address.get('street_optional'))
            setattr(self, 'shipping_address_city', shipping_address.get('city'))
            setattr(self, 'shipping_address_state', shipping_address.get('state'))
            setattr(self, 'shipping_address_zip_code', shipping_address.get('zip_code'))

        billing_address = obj.get('billing_address')
        
        if billing_address is not None:
            setattr(self, 'billing_address_street', billing_address.get('street'))
            setattr(self, 'billing_address_street_optional', billing_address.get('street_optional'))
            setattr(self, 'billing_address_city', billing_address.get('city'))
            setattr(self, 'billing_address_state', billing_address.get('state'))
            setattr(self, 'billing_address_zip_code', billing_address.get('zip_code'))
        
        credit_card = obj.get('credit_card')

        if credit_card is not None:
            setattr(self, 'credit_card_cardholder_name', credit_card.get('cardholder_name'))
            setattr(self, 'credit_card_card_number', credit_card.get('card_number'))
            setattr(self, 'credit_card_expiration_date', credit_card.get('expiration_date'))
            setattr(self, 'credit_card_cvv', credit_card.get('cvv'))

        return self
    
    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'shipping_address': {
                'street': self.shipping_address_street,
                'street_optional': self.shipping_address_street_optional,
                'city': self.shipping_address_city,
                'state': self.shipping_address_state,
                'zip_code': self.shipping_address_zip_code
            },
            'billing_address': {
                'street': self.billing_address_street,
                'street_optional': self.billing_address_street_optional,
                'city': self.billing_address_city,
                'state': self.billing_address_state,
                'zip_code': self.billing_address_zip_code,
            },
            'credit_card': {
                'cardholder_name': self.credit_card_cardholder_name,
                'card_number': self.credit_card_card_number,
                'expiration_date': self.credit_card_expiration_date,
                'cvv': self.credit_card_cvv
            }
        }