from flask import Flask
from flask_restful import Api
from api.ProductController import ProductController
from utils.constants import PRODUCTS_PATH
from data.init import *


app = Flask(__name__)
api = Api(app)

api.add_resource(ProductController, PRODUCTS_PATH)

if __name__ == '__main__':
  app.run(
    port=8080,
    debug=True
  )
