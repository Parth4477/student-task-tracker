import os
import sqlite3

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)
DB_PATH = os.environ.get("DB_PATH", "tasks.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS tasks ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "title TEXT NOT NULL, "
            "done INTEGER NOT NULL DEFAULT 0)"
        )


@app.route("/")
def home():
    with get_db() as conn:
        tasks = conn.execute("SELECT * FROM tasks ORDER BY done, id DESC").fetchall()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        with get_db() as conn:
            conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    return redirect(url_for("home"))


@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id):
    with get_db() as conn:
        conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    with get_db() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for("home"))


@app.route("/health")
def health():
    return jsonify(status="ok")


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
