from src.data.entities import Product
from src.data.repositories.product_repository import *


def get_products(query_object: dict):
    products: list[Product]
    products = get_products_from_db(query_object)
    products = [x.to_dict() for x in products]

    return products