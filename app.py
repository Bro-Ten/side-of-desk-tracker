from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    opportunities = conn.execute(
        "SELECT * FROM opportunities"
    ).fetchall()
    conn.close()
    return render_template("index.html", opportunities=opportunities)


@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        title = request.form["title"]
        lead = request.form["lead"]
        description = request.form["description"]
        roles = request.form["roles"]
        hours = request.form["hours"]

        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO opportunities (title, lead, description, roles, hours)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, lead, description, roles, hours),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
