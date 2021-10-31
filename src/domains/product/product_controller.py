from flask import Blueprint, abort
from utils.constants import PRODUCTS_PATH

products_controller = Blueprint('products', __name__)

@products_controller.route(PRODUCTS_PATH)
def get_products():
  return 'Products'
