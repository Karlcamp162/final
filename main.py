from tkinter import *
from connection import *
from tkinter import messagebox
from data import *
from block_windowz import blockA_window, blockB_window, blockC_window, blockD_window
from tkinter import font as tkFont

# Initialize blocks and instructors
create_blocks()
create_instructors()

block_win = None

def blocks_window():
    global block_win
    root.withdraw()  # Hide the root window
    block_win = Toplevel()
    block_win.geometry('400x250')
    block_win.config(bg='bisque')
    block_win.title('Choose a Block')
    
    Label(block_win, text='Choose Block', font=('Arial', 14, 'bold'), bg='bisque').pack(pady=20)
    
    # Using grid layout for better placement
    buttons_frame = Frame(block_win, bg='bisque')
    buttons_frame.pack(pady=10)
    
    Button(buttons_frame, text='Block A', command=blockA_window, bg='lightblue', font=('Arial', 12), width=10).grid(row=0, column=0, padx=10, pady=10)
    Button(buttons_frame, text='Block B', command=blockB_window, bg='lightgreen', font=('Arial', 12), width=10).grid(row=0, column=1, padx=10, pady=10)
    Button(buttons_frame, text='Block C', command=blockC_window, bg='lightcoral', font=('Arial', 12), width=10).grid(row=1, column=0, padx=10, pady=10)
    Button(buttons_frame, text='Block D', command=blockD_window, bg='lightyellow', font=('Arial', 12), width=10).grid(row=1, column=1, padx=10, pady=10)
    
    Button(block_win, text='Log out', command=logout, bg='red', font=('Arial', 12), width=10).pack(side=BOTTOM, pady=10)

def logout():
    block_win.destroy()  # Close the block window
    root.deiconify()  # Show the login window again

def login():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT username, password FROM instructors')
    instructor = cur.fetchone()
    
    if instructor and instructor[0] == username_entry.get() and instructor[1] == password_entry.get():
        blocks_window()
    else:
        messagebox.showerror('Error', "Username or password is incorrect.")


def main():
    global username_entry, password_entry, root
    root = Tk()
    root.geometry('500x400')
    root.title('Login')
    root.config(bg='#2C3E50')  # Dark blue-gray background for modern look

    # Create a custom font for the title
    title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")

    # Header Frame for a sleek background
    header_frame = Frame(root, bg='#1ABC9C', height=80)  # Aqua color
    header_frame.pack(fill=X)

    title_label = Label(header_frame, text='BARAT', font=title_font, fg='white', bg='#1ABC9C', pady=7)
    title_label.pack(pady=5)

    # Shadow Effect
    shadow_label = Label(header_frame, text='BARAT', font=title_font, fg='black', bg='#1ABC9C')
    shadow_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    shadow_label.lower()

    login_frame = Frame(root, bg='white', padx=10, pady=10)
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(login_frame, text='Username:', font=('Arial', 12), bg='white').grid(column=0, row=0, padx=5, pady=5, sticky=E)
    username_entry = Entry(login_frame, font=('Arial', 12))
    username_entry.grid(column=1, row=0, padx=5, pady=5, sticky=W)

    Label(login_frame, text='Password:', font=('Arial', 12), bg='white').grid(column=0, row=1, padx=5, pady=5, sticky=E)
    password_entry = Entry(login_frame, show='*', font=('Arial', 12))
    password_entry.grid(column=1, row=1, padx=5, pady=5, sticky=W)

    button_frame = Frame(login_frame, bg='white')
    button_frame.grid(column=0, row=2, columnspan=2, pady=10)

    Button(button_frame, text='Login', command=login, bg='#3498DB', fg='white', font=('Arial', 12), width=10).grid(column=0, row=0, padx=5)
    Button(button_frame, text='Exit', command=lambda: root.destroy(), bg='#E74C3C', fg='white', font=('Arial', 12), width=10).grid(column=1, row=0, padx=5)

    root.mainloop()

main()
