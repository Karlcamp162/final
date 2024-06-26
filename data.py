from connection import *


def a_students():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("select * from block_a")
    records = cur.fetchall()
    conn.commit()
    return records
    
def b_students():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("select * from block_b")
    records = cur.fetchall()
    conn.commit()
    
    return records
    
def c_students():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("select * from block_c")
    records = cur.fetchall()
    conn.commit()
    
    return records
    
def d_students():
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("select * from block_d")
    records = cur.fetchall()
    conn.commit()
    
    return records


# conn = create_connection()
# cur = conn.cursor()

# cur.execute('''
#             insert into block_a(student_id,last_name,first_name,yr_block)
#             values
#             (123456, 'surname1', 'firstname1', '2csa')
#             ''')
# conn.commit()
# conn.close()

# a = a_students()
# print(a)  

