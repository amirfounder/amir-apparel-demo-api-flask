from src.api.app import app
from src.data.seed import seed_data
from src.data.setup import setup_schema


def main():
  setup_schema()
  seed_data()
  app.run(port=8085, debug=True, use_reloader=False)


if __name__ == '__main__':
  main()