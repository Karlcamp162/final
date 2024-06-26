import sqlite3
import pandas as pd
from tkinter import messagebox

def export_to_excel(table):
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    sqlquery = f"select * from {table}"
    cursor.execute(sqlquery)
    result = cursor.fetchall()
    for row in result:
        df = pd.read_sql_query(sqlquery, connection)
        df.to_csv('block_a.csv', index = True, header = True)
    connection.close()   
        
    messagebox.showinfo("Success","Data Imported")