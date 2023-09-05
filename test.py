from flask import Flask, abort, render_template, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

# Rendering the "index" template
@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

# Default layout
@app.route("/default")
def default():
    return render_template("layout.html")

# Looping through list
@app.route("/about/")
def about():
    sites = ["twitter", "facebook", "instagram", "whatsapp"]
    return render_template("about.html", sites = sites)

# Rendering the "home" template
@app.route("/home/")
def home():
    return render_template("home.html")

# If Statement testing different user-inputter roles
@app.route("/contact/<role>")
def contact(role):
    return render_template("contact.html", person = role)

# Multiple If Statements redirecting to other pages
@app.route("/choice/<pick>")
def choice(pick):
    if pick == 'variable':
        return redirect(url_for('var'))
    if pick == 'if':
        return redirect(url_for('ifelse'))
    if pick == 'for':
        return redirect(url_for('for_loop'))

if __name__ == "__main__":
    app.run()

# Capitalizing a user-inputted variable
# @app.route("/capitalize/<word>/")
# def capitalize(word):
#     return "<h1>{}</h1>".format(escape(word.capitalize()))

# Mathematical operation applied to user-inputted variables
# @app.route("/add/<int:n1>/<int:n2>/")
# def add(n1, n2):
#     return "<h1>{}</h1>".format(n1 + n2)

# Try and Except block for user-inputted variable
# @app.route("/users/<int:user_id>/")
# def greet_user(user_id):
#     users = ["Bob", "Jane", "Adam"]
#     try:
#         return "<h2>Hi {}</h2>".format(users[user_id])
#     except IndexError:
#         abort(404)
        
# Capitalizing a user-inputter name
# @app.route("/<name>/")
# def welcome(name):
#     name = escape(name.capitalize())
#     return render_template("welcome.html", name = name)

