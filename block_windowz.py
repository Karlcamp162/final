from tkinter import *
from tkinter import ttk, messagebox
from connection import create_connection
from add_date import add_date_window, insert_data, delete_data, update_combobox
from get_column import get_column_names  # Importing from the new module
from dtbToCSV import export_to_excel

def blockA_window():
    existing_columns = get_column_names('block_a')
    conn = create_connection()

    window_a = Toplevel()
    window_a.title('Block A Window')
    window_a.attributes('-fullscreen', True)
    window_frame = Frame(window_a)
    window_frame.pack(side=LEFT)

    btn_date = Button(window_frame, text="Date Input", font=('Roboto', 12), width=8, 
                      command=lambda: add_date_window(tree, 'block_a'))
    btn_date.pack(pady=10)

    Button(window_frame, text="Back", font=("Roboto", 12), width=8, 
                command=lambda:window_a.destroy()).pack(pady=5)
    
    Button(window_frame, text="Export", font=("Roboto", 12), width=8, 
                command=lambda: export_to_excel('block_a')).pack()
    

    tree = ttk.Treeview(window_a, columns=(existing_columns), show="headings")
    for col in existing_columns:
        tree.heading(col, text=col)
    
    column_combobox = ttk.Combobox(window_frame, font=("Roboto", 12), width=8)
    column_combobox.pack(pady=5)
    Button(window_frame, text="Delete Column", font=("Roboto", 12), width=8,
           command=lambda: delete_data(tree, 'block_a', column_combobox)).pack()
    update_combobox(column_combobox, 'block_a')
        
    v_scroll = ttk.Scrollbar(window_a, orient=VERTICAL, command=tree.yview)
    h_scroll = ttk.Scrollbar(window_a, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.configure(xscrollcommand=h_scroll.set)
    v_scroll.pack(side=RIGHT, fill=Y)
    h_scroll.pack(side=BOTTOM, fill=X)
    
    tree.pack(expand=True, fill="both")

    insert_data(tree, 'block_a')
    conn.commit()
    

def blockB_window():
    existing_columns = get_column_names('block_b')       
    conn = create_connection()

    window_b = Toplevel()
    window_b.title('Block B Window')
    window_b.attributes('-fullscreen', True)
    window_frame = Frame(window_b)
    window_frame.pack(side=LEFT)

    btn_date = Button(window_frame,text="Date Input",font=('Roboto',12),width=8, command= lambda: add_date_window(tree, 'block_b'))
    btn_date.pack(pady=10)

    Button(window_frame, text="Back", font=("Roboto", 12), width=8, 
                command=lambda:window_b.destroy()).pack(pady=5)
    
    Button(window_frame, text="Export", font=("Roboto", 12), width=8, 
                command= lambda: export_to_excel('block_b')).pack()

    tree = ttk.Treeview(window_b, columns=(existing_columns), show="headings")
    
    column_combobox = ttk.Combobox(window_frame, font=("Roboto", 12), width=8)
    column_combobox.pack(pady=5)
    Button(window_frame, text="Delete Column", font=("Roboto", 12), width=8,
           command=lambda: delete_data(tree, 'block_b', column_combobox)).pack()
    update_combobox(column_combobox, 'block_b')
    # Define the headings
    for col in existing_columns:
        tree.heading(col, text=col)
    
    v_scroll = ttk.Scrollbar(window_b, orient=VERTICAL, command=tree.yview)
    h_scroll = ttk.Scrollbar(window_b, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.configure(xscrollcommand=h_scroll.set)
    v_scroll.pack(side=RIGHT, fill=Y)
    h_scroll.pack(side=BOTTOM, fill=X)
    
    tree.pack(expand=True, fill="both")

    insert_data(tree, 'block_b')
    conn.commit()
    
def blockC_window():
    existing_columns = get_column_names('block_c')
    conn = create_connection()

    window_c = Toplevel()
    window_c.title('Block C Window')
    window_c.attributes('-fullscreen', True)
    window_frame = Frame(window_c)
    window_frame.pack(side=LEFT)

    btn_date = Button(window_frame,text="Date Input",font=('Roboto',12),width=8, command= lambda: add_date_window(tree, 'block_c'))
    btn_date.pack(pady=10)

    Button(window_frame, text="Back", font=("Roboto", 12), width=8, 
                command=lambda:window_c.destroy()).pack(pady=5)
    
    Button(window_frame, text="Export", font=("Roboto", 12), width=8, 
                command= lambda: export_to_excel('block_c')).pack()

    tree = ttk.Treeview(window_c, columns=(existing_columns), show="headings")
    column_combobox = ttk.Combobox(window_frame, font=("Roboto", 12), width=8)
    column_combobox.pack(pady=5)
    Button(window_frame, text="Delete Column", font=("Roboto", 12), width=8,
           command=lambda: delete_data(tree, 'block_c', column_combobox)).pack()
    update_combobox(column_combobox, 'block_c')
    # Define the headings
    for col in existing_columns:
        tree.heading(col, text=col)
        
    v_scroll = ttk.Scrollbar(window_c, orient=VERTICAL, command=tree.yview)
    h_scroll = ttk.Scrollbar(window_c, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.configure(xscrollcommand=h_scroll.set)
    v_scroll.pack(side=RIGHT, fill=Y)
    h_scroll.pack(side=BOTTOM, fill=X)
    
    tree.pack(expand=True, fill="both")

    insert_data(tree, 'block_c')
    conn.commit()


def blockD_window():
    existing_columns = get_column_names('block_d')
    conn = create_connection()

    window_d = Toplevel()
    window_d.title('Block D Window')
    window_d.attributes('-fullscreen', True)
    window_frame = Frame(window_d)
    window_frame.pack(side=LEFT)

    btn_date = Button(window_frame,text="Date Input",font=('Roboto',12),width=8, command= lambda: add_date_window(tree, 'block_d'))
    btn_date.pack(pady=10)

    Button(window_frame, text="Back", font=("Roboto", 12), width=8, 
                command=lambda:window_d.destroy()).pack(pady=5)
    
    Button(window_frame, text="Export", font=("Roboto", 12), width=8, 
                command= lambda: export_to_excel('block_d')).pack()

    tree = ttk.Treeview(window_d, columns=(existing_columns), show="headings")
    column_combobox = ttk.Combobox(window_frame, font=("Roboto", 12), width=8)
    column_combobox.pack(pady=5)
    Button(window_frame, text="Delete Column", font=("Roboto", 12), width=8,
           command=lambda: delete_data(tree, 'block_d', column_combobox)).pack()
    update_combobox(column_combobox, 'block_d')
    # Define the headings
    for col in existing_columns:
        tree.heading(col, text=col)
    
    v_scroll = ttk.Scrollbar(window_d, orient=VERTICAL, command=tree.yview)
    h_scroll = ttk.Scrollbar(window_d, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.configure(xscrollcommand=h_scroll.set)
    v_scroll.pack(side=RIGHT, fill=Y)
    h_scroll.pack(side=BOTTOM, fill=X)
    
    tree.pack(expand=True, fill="both")

    insert_data(tree, 'block_d')
    conn.commit()
