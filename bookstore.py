import sqlite3
def create_database():
    conn = sqlite3.connect("book_store.db")  
    cursor = conn.cursor()
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price text 
        )
    ''')

    conn.commit()
    conn.close()

create_database()

def book_entry(title, price, ):
    """
    Inserts book data into the database.
    """
    conn = sqlite3.connect("book_store.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM book WHERE title= ?
    ''', (title,))

    result = cursor.fetchone()
    if result[0] >0:
        print('data exists')
        return

    
    cursor.execute('''
        INSERT INTO book ('title', 'price')
        VALUES (?, ?)
    ''', (title, price))
    
    conn.commit()
    conn.close()
    print(f"Data inserted: {title}" )
    print(f"Data inserted:  { price}" )
    