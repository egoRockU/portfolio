import os
from flask import Flask, render_template, json, request
from utils.search import search
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv()
app.config['GITHUB_TOKEN'] = os.getenv('GITHUB_TOKEN')

@app.route("/")
def home():
    file = os.path.join(app.static_folder, 'data', 'projects.json')
    with open(file) as test_file:
        data = json.load(test_file)
    threeProj = { k: data[k] for k in list(data.keys())[:3] }
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
    return render_template('projects.html', title="Projects")

@app.route("/getprojects", methods = ['GET', 'POST'])
def get_projects():
    file = os.path.join(app.static_folder, 'data', 'projects.json')
    with open(file) as test_file:
        projects = json.load(test_file)

    if request.method == 'POST':
        entry = request.form['entry']
        projects = search(projects, entry)

    return render_template('projectsView.html', projects=projects)

@app.route("/getrepos")
def get_repos():
    url = 'https://api.github.com/users/egoRockU/repos?sort=pushed'
    headers = {'Authorization': 'Bearer ' + app.config['GITHUB_TOKEN']}
    repos = requests.get(url, headers=headers).json()
    first_five_repos = repos[:5]
    
    return render_template('repos.html', repos = first_five_repos)

if __name__ == '__main__':
    app.run(debug=True)