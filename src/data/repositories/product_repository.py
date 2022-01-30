from operator import or_
from sqlalchemy import func
from src.data.entities import Product
from src.data.setup import build_session

def get_products_from_db(query_object: dict):
    session = build_session()

    query = session.query(Product)
    query = query.filter()

    for key, values in query_object.items():
        attribute = getattr(Product, key)

        comparator_left = func.lower(attribute)
        comparator_ors = []

        for value in values:

            if isinstance(value, str):
                value = func.lower(value)
            
            comparator_right = value
            comparator_equal = comparator_left == comparator_right
            comparator_ors.append(comparator_equal)

        while len(comparator_ors) > 1:
            comparator_ors[0] = or_(*comparator_ors[:2])
            comparator_ors.pop(1)

        comparator = comparator_ors[0]
        query = query.filter(comparator)

    query = query.order_by(Product.id.asc())

    products = query.all()
    
    session.close()
    session.commit()

    return products