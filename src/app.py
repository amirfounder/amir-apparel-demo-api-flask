from re import I
from flask import Flask
from domains.product.product_controller import products_controller


app = Flask(__name__)

app.register_blueprint(products_controller)

if __name__ == '__main__':
  app.run()

