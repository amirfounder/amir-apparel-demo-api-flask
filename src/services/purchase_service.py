from src.data.entities import Purchase
from src.data.repositories.purchase_repository import create_purchase_to_db

def create_purchase_service(data: str):
    purchase_to_create: Purchase
    purchase_to_create = Purchase()
    purchase_to_create = purchase_to_create.from_dict(data)

    purchase: Purchase
    purchase = create_purchase_to_db(purchase_to_create)

    created_purchase: dict
    created_purchase = purchase.to_dict()

    return created_purchase

