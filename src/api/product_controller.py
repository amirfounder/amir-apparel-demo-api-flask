from flask import request
from src.api.app import app
from src.data.entities import Product
from src.services.product_service import get_products as get_products_service
from src.utils.utils import build_query_object, build_query_string, clean_query_object, responsify


@app.route('/products/filter', methods=['GET'])
def get_products():
    accepted_filters = ['material', 'color', 'demographic', 'type']

    query_string = build_query_string(request)
    query_object = build_query_object(query_string)
    query_object = clean_query_object(accepted_filters, query_object)

    products = list[dict]
    products = get_products_service(query_object)

    response = responsify(products)
    response.status = 200

    return response
