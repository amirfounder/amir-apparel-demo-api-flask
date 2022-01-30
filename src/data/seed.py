from src.data.entities import Product
from src.data.factory import build_products
from src.data.setup import build_session


def seed_data():

    session = build_session()
    existing_products = session.query(Product).all()

    if len(existing_products) != 0:
        return

    products: list[Product]
    products = build_products(500)

    session = build_session()
    session.add_all(products)
    session.commit()
    session.close()
