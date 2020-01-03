import importlib
api = importlib.import_module('api')

if __name__ == "__main__":
    api.app.run()