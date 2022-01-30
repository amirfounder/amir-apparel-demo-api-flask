from src.data.entities import Product
from src.data.repositories.product_repository import *
from src.utils.http_exceptions import throw_not_found


def get_products_service(query_object: dict):
    products: list[Product]
    products = get_products_from_db(query_object)
    products = [x.to_dict() for x in products]

    return products


def get_product_by_id_service(id: int):
    product: Product
    product = get_product_by_id_from_db(id)

    if product is None:
        message = 'Could not find product with ID: {}'.format(id)
        throw_not_found(message)
    
    product = product.to_dict()
    return product