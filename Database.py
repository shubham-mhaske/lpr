import sqlite3
from sqlite3 import Error
import io
import paths
import PIL

conn = None


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    global  conn
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print('Connection created successfully')

def close_db():
    if conn:
        conn.close()
        print('connection closed successfully')

def create_vehicle_data_table():
    query = '''
            CREATE TABLE vehicle_data ( vehicle_id INTEGER TEXT KEY,
             name TEXT NOT NULL,
             contact_no TEXT NOT NULL,
             address TEXT NOT NULL,
              photo BLOB NOT NULL);
            '''
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

def insert_data(id,name,contact_no,address,image):
    insert_query = '''
                    INSERT INTO vehicle_data VALUES(
                    ?,?,?,?,?);
                    '''
    cursor = conn.cursor()
    cursor.execute(insert_query,(id,name,contact_no,address,image))
    conn.commit()
    cursor.close()
def get_data(id):
    get_query = '''
                SELECT photo FROM vehicle_data
                WHERE vehicle_id = ?;
                '''
    cursor = conn.cursor()
    cursor.execute(get_query,(id,))
    data = cursor.fetchall()[0][0]
    file_like = io.BytesIO(data)
    img = PIL.Image.open(file_like)
    img.save('./static/detected.jpg')

    cursor.close()
    return img
#create_vehicle_data_table()

def query_all():
    query = '''
            SELECT * FROM vehicle_data
            '''
    cur = conn.cursor()
    cur.execute(query)
    print(cur.fetchall())
    cur.close()
