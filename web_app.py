from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return "<h1>Hello, World!</h1>"

@app.route("/about/")
def about():
    return "<h3>About Page</h3>"

@app.route("/capitalize/<word>/")
def capitalize(word):
    return "<h1>{}</h1>".format(escape(word.capitalize()))

if __name__ == "__main__":
    app.run()
    
