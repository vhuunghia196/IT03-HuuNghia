import json

from flask import Flask


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    load_categories.run(debug=True)

app = Flask(__name__)

