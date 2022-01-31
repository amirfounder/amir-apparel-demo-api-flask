from src.data.entities import Purchase
from src.data.setup import build_session


def create_purchase_to_db(purchase_to_create: Purchase):

    session = build_session()
    session.add(purchase_to_create)
    session.commit()
    session.close()

    return purchase_to_create
     