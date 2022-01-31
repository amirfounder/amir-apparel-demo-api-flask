from flask import request
from src.api.app import app
from src.services.purchase_service import *
from src.utils.utils import convert_request_body_to_snakecase, responsify


@app.route('/purchases', methods=['POST'])
def create_purchase():
    data = request.json
    data = convert_request_body_to_snakecase(data)

    purchase: dict
    purchase = create_purchase_service(data)

    response = responsify(purchase)
    response.status = 200

    return response
