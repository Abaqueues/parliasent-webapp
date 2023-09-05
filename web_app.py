from flask import Flask, abort, render_template, redirect, url_for
from markupsafe import escape
from sqlalchemy import create_engine
import psycopg2 as ps2

app = Flask(__name__)

_DATABASE_URL = "postgresql://postgres:password@127.0.0.1:5432/predicted_data"
conn = ps2.connect(_DATABASE_URL)

@app.route("/")
@app.route("/index/")
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM speech_data")
    data = cursor.fetchall()
    cursor.close()
    return render_template("index.html", data = data)

@app.teardown_appcontext
def close_connection(exception):
    conn.close()

if __name__ == "__main__":
    app.run()
    