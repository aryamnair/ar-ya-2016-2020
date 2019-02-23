from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "hello...."

@app.route("/")
def home():
    return "My Home page"

@app.route("/")
def contact():
    return "My Contact page"

if(__name__=="__main__"):
    app.run()