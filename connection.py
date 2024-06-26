import sqlite3

def create_connection():
    conn = sqlite3.connect('attendance.db')
    conn.commit()
    return conn

def create_blocks():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute('''
                create table if not exists block_a(
                    student_id int, 
                    last_name varchar(225), 
                    first_name varchar(225), 
                    yr_block varchar(20) 
                    )
                ''')
    cur.execute('''
                create table if not exists block_b(
                    student_id int, 
                    last_name varchar(225), 
                    first_name varchar(225), 
                    yr_block varchar(20) 
                    )
                ''')
    cur.execute('''
                create table if not exists block_c(
                    student_id int, 
                    last_name varchar(225), 
                    first_name varchar(225), 
                    yr_block varchar(20) 
                    )
                ''')
    cur.execute('''
                create table if not exists block_d(
                    student_id int, 
                    last_name varchar(225), 
                    first_name varchar(225), 
                    yr_block varchar(20) 
                    )
                ''')
    conn.commit()
    conn.close()
    

def create_instructors():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
                create table if not exists instructors(
                    username varchar(225),
                    password varchar(225)
                )
                ''')
    conn.commit()
    conn.close()

def add_date():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute('''
                alter table block_a
                add column ? date;
                ''')
        
    conn.commit()