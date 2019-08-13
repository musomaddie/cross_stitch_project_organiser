import sqlite3


MY_DATABASE = "db/Cross_Stitch_Supplies.db"


def _check_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def add_new_thread(thread_name, amount_have):
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    if not _check_number(amount_have):
        return False
    try:
        cur.execute(""" INSERT INTO threads
                        VALUES (?, ?);""", (thread_name, amount_have))
    except Exception:
        return False
    conn.commit()
    cur.close()
    conn.close()
    return True
