from flask import Flask
from src.data.seed import seed_data
from src.data.setup import setup_schema


app = Flask(__name__)


def run_app():
  setup_schema()
  seed_data()
  app.run(port=8080)