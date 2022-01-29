from flask import Flask

from src.data.setup import setup_schema


app = Flask(__name__)


def run_app():
  setup_schema()
  app.run(port=8080, debug=True)