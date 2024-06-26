from connection import create_connection

def get_column_names(table):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    columns = [info[1] for info in cur.fetchall()]
    conn.commit()
    return columns
