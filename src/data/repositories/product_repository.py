from operator import or_
from sqlalchemy import func
from src.data.entities import Product
from src.data.setup import build_session

def get_products_from_db(query_object: dict):
    session = build_session()

    query = session.query(Product)
    query = query.filter()

    for key, values in query_object.items():
        attribute_access = getattr(Product, key)

        comparator_left = attribute_access
        comparator_ors = []

        for value in values:

            comparator_right = func.lower(value) if isinstance(value, str) else value
            comparator_equal = comparator_left == comparator_right
            comparator_ors.append(comparator_equal)

        comparator = or_(*comparator_ors)
        query = query.filter(comparator)

    query = query.order_by(Product.id.asc())

    products = query.all()
    
    session.close()
    session.commit()

    return products