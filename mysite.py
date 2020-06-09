from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to My site"

@app.route("/site")
def site():
    return """<html><head><title>mysite</title></head><body bgcolor="green"><h1> Welcome to my site </h1></html>"""

@app.route("/repos")
def getRepos():
    username = 'user'
    token = 'token'

    response = requests.get('https://api.github.com/search/repositories?q=github+api')

    return response.content