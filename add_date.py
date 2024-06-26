from tkinter import *
from connection import *
import re
import cv2
import threading
from tkinter import *
from pyzbar.pyzbar import decode
from tkinter import messagebox
from connection import create_connection
from get_column import get_column_names
import time

def insert_data(tree, table):
    conn = create_connection()
    cur = conn.cursor()
    for i in tree.get_children():
        tree.delete(i)
        
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    
    #sort the data by last name
    data = list(rows)
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][1] > data [j+1][1]:
                data[j], data[j+1] = data[j+1], data[j]
    
    #insert sorted data into the treeview
    for row in data:
        tree.insert("", END, values=row)

#Add Column ibn the treeview depends on the user's column name
def get_column_names(table):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    columns = [info[1]for info in cur.fetchall()]
    conn.commit()
    return columns

new_columns = []
def add_column(tree, current_block):
    add = date_Entry.get().strip()
    if not add:
        messagebox.showerror("Input Error", "Please enter a column name.")
        return
    
    current_columns = get_column_names(current_block)
    if add in current_columns:
        messagebox.showerror("Duplicate Error", "Column already exists.")
        return
    
    new_column_name = add
    current_columns.append(new_column_name)
    tree.config(columns=current_columns)
    tree.heading(new_column_name, text=new_column_name)
    for col in current_columns:
        tree.heading(col, text=col)
    
    if add_column_to_database(new_column_name, current_block):
        # Open the barcode scanner
        threading.Thread(target=BARAS, 
                         args=(new_column_name, current_block, display_label)).start()

def delete_data(tree, table, column_combobox):
    conn = create_connection()
    cur = conn.cursor()
    selected_column = column_combobox.get()
    
    if not selected_column:
        messagebox.showerror("Selected Error","Please select a column to delete.")
        return
    
    #Check if the column to delete is a mandatory column(kung unoy imo sa database amoy sa treeview)
    if selected_column in['Student_ID','lastname','firstname','Block','time_in']:
        messagebox.showerror("Selection Error","Selected column cannot be delete.")
        return
    
    try:
        cur.execute(f"ALTER TABLE {table} DROP COLUMN '{selected_column}'")
        conn.commit()
        messagebox.showinfo("Success",f"Column'{selected_column}' deleted successfully." )
        if selected_column in new_columns:
            new_columns.remove(selected_column)
    except sqlite3.Error as e:
        messagebox.showerror("Error",f"An Error Occurred: {e}")
        
    # UPdate the Tre3eview columns
    current_columns = get_column_names(table)
    tree.config(columns=current_columns)
    for col in current_columns:
        tree.heading(col, text=col)

    update_combobox(column_combobox, table)
    
def update_combobox(column_combobox, table):
    current_columns = get_column_names(table)
    column_combobox['values'] = current_columns
    

def add_column_to_database(column_name, table):
    conn = create_connection()
    cur = conn.cursor()
    column_type = "TEXT"
    try:
        if re.match(r"^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/(\d{4})$", column_name):
            cur.execute(f"ALTER TABLE {table} add column '{column_name}' {column_type};")
            conn.commit()
            messagebox.showinfo("Success",f"Column '{column_name}' added to the database successfully.")
            return True
        else:
            raise ValueError(messagebox.showerror('Error', "Invalid column name format. Must be in MM/DD/YYYY format."))
        #Quote teh column name to handle special character
    except sqlite3.Error as e:
        messagebox.showerror("Error",f"An Error occurred: {e}")
    

def add_date_window(tree, current_block):
    global date_Entry, add_win, display_label
    add_win = Toplevel()
    add_win.geometry('400x250')
    
    Label(add_win, text='Enter date to add: ', font=('roboto', 12)).grid(column=0, row=0)
    date_Entry = Entry(add_win)
    date_Entry.grid(column=1, row=0)
    
    confirm_button = Button(add_win, text='Confirm', font=('roboto', 12),
                            command=lambda: add_column(tree, current_block))
    confirm_button.grid(column=1, row=1)
    Button(add_win, text='Cancel', font=('roboto', 12), command=lambda:add_win.destroy()).grid(column=2, row=1)
    
    display_label = Label(add_win, text='Scanned ID: ', font=('roboto', 12))
    display_label.grid(column=0, row=2, columnspan=2, pady=10)
    

def BARAS(date_column, table, display_label):
    # Open the video stream
    cap = cv2.VideoCapture(0)
    
    user_database = {
        "480110123456": {"ID": "123456", 'Last_name': 'Surname1', 'First_name': 'Firstname1', 'Block': '2CSA'}, 
        "480110654321": {"ID": "654321", 'Last_name': 'Surname2', 'First_name': 'Firstname2', 'Block': '2CSA'},
        "480110231456": {"ID": "231456", 'Last_name': 'Abaca', 'First_name': 'Alex', 'Block': '2CSA'},
        "480110236541": {"ID": "236541", 'Last_name': 'Zuza', 'First_name': 'Flex', 'Block': '2CSA'},
        "480110231234": {"ID": "231234", 'Last_name': 'Waza', 'First_name': 'Bits', 'Block': '2CSA'},
        # Add more entries as needed
    }

    conn = create_connection()
    cur = conn.cursor()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            if barcode_data in user_database:
                student_id = user_database[barcode_data]["ID"]
                student_first = user_database[barcode_data]["First_name"]
                student_last = user_database[barcode_data]["Last_name"]
                student_block = user_database[barcode_data]["Block"]
                try:
                    cur.execute(f"UPDATE {table} SET '{date_column}' = 'Present' WHERE student_id = ?", (student_id,))
                    conn.commit()
                    print(f"Student {student_id} marked as present.")
                    
                    # Update the display label
                    display_label.config(text=f"Scanned ID: {student_id}\n First Name: {student_first}\n Last name: {student_last}\n Year/Block: {student_block}")
                    
                    # Pause for 1 second
                    time.sleep(1)
                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")

        cv2.imshow('Barcode Scanner', frame)
        
        # Press 'q' to quit the scanner
        if cv2.waitKey(1) & 0xFF == ord('q'):
            add_win.destroy()
            break

    cap.release()
    cv2.destroyAllWindows()
    conn.close()
