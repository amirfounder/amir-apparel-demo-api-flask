from src.data.entities import Product
from src.data.setup import build_session

def get_products_from_db():
    session = build_session()

    query = session.query(Product)
    query = query.order_by(Product.id.asc())

    products = query.all()
    
    session.close()
    session.commit()

    return products