from connection import create_connection
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import sqlite3


def delete_data(tree):
    conn = create_connection()
    cur = conn.cursor()
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Selected Error","Please select an item to delete.")
        return
    
    item = tree.item(selected_item)
    student_id = item['values'][0]
    
    
    #Delete data from the database
    try:
        cur.execute("DELETE FROM table_name WHERE Student_id = ?",(student_id,))
        conn.commit()
        messagebox.showinfo("Success","Data Deleted Successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error",f"An error occurred: {e}")
        
    
    tree.delete(selected_item)