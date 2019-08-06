import sqlite3


def init_db():
    db_name = "Cross_Stitch_Supplies"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # DROP TABLES
    cur.execute("""DROP TABLE IF EXISTS threads""")

    # THREADS
    cur.execute('''
                CREATE TABLE threads (
                    colour TEXT PRIMARY KEY,
                    amount FLOAT
                );
            ''')


if __name__ == '__main__':
    init_db()
