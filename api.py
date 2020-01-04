import importlib
from flask import Flask, jsonify, request, render_template

LetteredTabs = importlib.import_module('LetteredTabs')

app = Flask(__name__,
            static_url_path='',
            static_folder='frontend',
            template_folder='frontend')


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/conversion', methods=['POST'])
def convert():
    converted = LetteredTabs.main(request.get_json()['input'])
    lettered = jsonify({"data": converted})
    return lettered, 200