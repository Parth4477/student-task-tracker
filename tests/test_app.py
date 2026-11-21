import os
import sys
import tempfile

# Use a throwaway database so tests never touch real data
_tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_tmp.close()
os.environ["DB_PATH"] = _tmp.name

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app as tracker  # noqa: E402


def get_client():
    tracker.app.config["TESTING"] = True
    return tracker.app.test_client()


def test_health():
    r = get_client().get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_home_page_loads():
    r = get_client().get("/")
    assert r.status_code == 200
    assert b"Student Task Tracker" in r.data


def test_add_task():
    c = get_client()
    c.post("/add", data={"title": "Finish DevOps report"})
    assert b"Finish DevOps report" in c.get("/").data


def test_empty_title_is_ignored():
    c = get_client()
    before = c.get("/").data.count(b'class="title"')
    c.post("/add", data={"title": "   "})
    assert c.get("/").data.count(b'class="title"') == before


def test_mark_done_and_delete():
    c = get_client()
    c.post("/add", data={"title": "Task to finish"})
    with tracker.get_db() as conn:
        task_id = conn.execute(
            "SELECT id FROM tasks WHERE title = ?", ("Task to finish",)
        ).fetchone()["id"]

    c.post(f"/done/{task_id}")
    with tracker.get_db() as conn:
        assert conn.execute("SELECT done FROM tasks WHERE id = ?", (task_id,)).fetchone()["done"] == 1

    c.post(f"/delete/{task_id}")
    with tracker.get_db() as conn:
        assert conn.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone() is None
