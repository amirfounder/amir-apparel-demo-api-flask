from src.api.app import app
from src.data.seed import seed_data
from src.data.setup import setup_schema


def run_app():
  setup_schema()
  seed_data()
  app.run(port=8080, debug=True, use_reloader=False)