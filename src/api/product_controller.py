from src.api.app import app
from src.services.product_service import get_products as get_products_service
from src.utils.utils import responsify


@app.route('/products', methods=['GET'])
def get_products():
    products = list[dict]
    products = get_products_service()

    response = responsify(products)
    response.status = 200

    return response
