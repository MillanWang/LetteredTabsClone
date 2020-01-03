import importlib
from flask import Flask, jsonify, request

LetteredTabs = importlib.import_module('LetteredTabs')

app = Flask(__name__)


@app.route('/conversion', methods=['POST'])
def convert():
    print(request)
    converted = LetteredTabs.main(request.get_json()['input'])
    lettered = jsonify({"data": converted})
    return lettered, 200