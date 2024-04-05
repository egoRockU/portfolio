import os
from flask import Flask, render_template, json, url_for
from flask.views import View

app = Flask(__name__)

@app.route("/")
def home():
    file = os.path.join(app.static_folder, 'data', 'projects.json')
    with open(file) as test_file:
        data = json.load(test_file)
    threeProj = { k: data[k] for k in list(data.keys())[:3] }
    print(data)
    return render_template("home.html", obj=threeProj)

@app.route("/skills")
def skills():
    file = os.path.join(app.static_folder, 'data', 'skills.json')
    with open(file) as test_file:
        data = json.load(test_file)
    obj = {
        'title': "Skills",
        'skills': data
    }
    return render_template("skills.html", obj=obj)


@app.route("/projects")
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)