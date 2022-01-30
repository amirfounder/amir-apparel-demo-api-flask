from src.data.entities import Product
from src.data.factory import build_products
from src.data.setup import build_session, reset_schema


def seed_data():

    reset_schema()

    products: list[Product]
    products = build_products(500)

    session = build_session()
    session.add_all(products)
    session.commit()
    session.close()
