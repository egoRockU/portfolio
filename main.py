import os
from flask import Flask, render_template, json, url_for
from flask.views import View

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/skills")
def skills():
    file = os.path.join(app.static_folder, 'data', 'skills.json')
    with open(file) as test_file:
        data = json.load(test_file)
    obj = {
        'title': "Skills",
        'skills': data
    }
    print(obj)
    return render_template("skills.html", obj=obj)


if __name__ == '__main__':
    app.run(debug=True)