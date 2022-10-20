from flask import render_template

from saleapp import app, dao


@app.route("/")
def index():
    categories = dao.load_categories()
    return render_template('index.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)

