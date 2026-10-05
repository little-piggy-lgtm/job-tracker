import json
import sqlite3

def init_db():
    conn=sqlite3.connect("data.db")
    sql="""CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    position TEXT,
    date TEXT,
    status TEXT
)"""
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def load():
    conn=sqlite3.connect("data.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM applications")
    rows=cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    records=[dict(zip(columns,row)) for row in rows]
    conn.close()
    return records


def save(records):
    conn=sqlite3.connect("data.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM applications")
    for record in records:
        cursor.execute(
            "INSERT INTO applications(company,position,date,status)VALUES(?,?,?,?)",
            (record["company"],record["position"],record["date"],record["status"])
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    save([
        {"company": "字节", "position": "后端", "date": "2025-01-01", "status": "已投"},
        {"company": "腾讯", "position": "前端", "date": "2025-01-02", "status": "笔试"}
    ])
    print(load())